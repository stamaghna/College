import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.ArrayList;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.*;
//javac -classpath ~/Desktop/apache-tomcat-9.0.40/lib/servlet-api.jar Ticketprice.java
public class Ticketprice extends HttpServlet
{
    
    public void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException 
	{

		var start=res.getParameter("stct");
		var end=res.getParameter("dtct");
		var date=res.getParameter("dt";)


		res.setContentType("text/html");
		PrintWriter out = res.getWriter();

		out.println("<!DOCTYPE HTML>\n<html>\n<head>\n<meta charset=\"UTF-8\">");
		out.println("<style> table, th, td {border: 1px solid black;} td {text-align: center;}</style>");
		out.println("<head><title>Ticket Price</title></head>");
		out.println("<body><h2>TICKET PRICE FOR YOU ONLY.</h2></body>");
		out.println("<table><tr>");
    	//out.println("<th>FLIGHT ID</th><th>START CITY</th><th>DEST CITY</th><th>PRICE</th></tr>");

		//Setting JDBC
		String dbClassName = "com.mysql.jdbc.Driver";
   		String url = "jdbc:mysql://127.0.0.1:3306/tommy";
    		String user = "root";
    		String password = "12345678";
        	try {
           	 Class.forName(dbClassName);
		 Connection con = DriverManager.getConnection(url, user, password);
            //console.log("Success");

//SQL STATEMENT
		Statement stmt = con.createStatement();
		String sql;
         	sql = "SELECT * FROM DISCOUNT;";
         	ResultSet rs = stmt.executeQuery(sql);
		while(rs.next()){
            //Retrieve by column name
//CREATE TABLE DISCOUNT(FLTID CHAR(3) PRIMARY KEY, STRTCT CHAR(15), DESTCT CHAR(15), PRICE INT, STDT DATE, ENDDT DATE);
		String flightid = rs.getString("FLTID");
     		String startct = rs.getString("STRTCT");
		String destct = rs.getString("DESTCT");
		int price = rs.getInt("PRICE");
		String startdt = rs.getDate("STDT").toString();
		String enddt = rs.getDate("ENDDT").toString();
		out.println("<tr><td>"+flightid+"</td>");
		out.println("<td>"+startct+"</td>");
		out.println("<td>"+destct+"</td>");
		out.println("<td>"+price+"</td></tr>");
         	}
        	} catch (Exception e) {
            //console.log(e.getMessage());
        	}
		out.println("</html");
		out.close();
	}
}

