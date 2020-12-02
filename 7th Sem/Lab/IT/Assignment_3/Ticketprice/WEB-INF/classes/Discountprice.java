import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.*;
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;   
//javac -classpath ~/Desktop/apache-tomcat-9.0.40/lib/servlet-api.jar Discountprice.java
public class Discountprice extends HttpServlet
{
  
    public void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException 
	{
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd");  
   		LocalDateTime now = LocalDateTime.now();
		String sysdate=dtf.format(now);

		res.setContentType("text/html");
		PrintWriter out = res.getWriter();

		//out.println(sysdate);

		out.println("<!DOCTYPE HTML>\n<html>\n<head>\n<meta charset=\"UTF-8\">");
		out.println("<style> table, th, td {border: 1px solid black;} td {text-align: center;}</style>");
		out.println("<head><title>Ticket Price</title></head>");
		out.println("<body><h2>DISCOUNTED TICKET PRICE</h1><br><h3>USE DISCOUNT TO GET COVID TEST DONE<h3></body>");

		//Setting JDBC
		String dbClassName = "com.mysql.jdbc.Driver";
   		String url = "jdbc:mysql://127.0.0.1:3306/tommy";
    	String user = "root";
    	String password = "12345678";
        try {
            Class.forName(dbClassName);
            Connection con = DriverManager.getConnection(url, user, password);

			out.println("<table><tr>");
    		out.println("<th>FLIGHT ID</th><th>START CITY</th><th>DEST CITY</th><th>PRICE</th></tr>");

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

			if(sysdate.compareTo(startdt) >= 0 && sysdate.compareTo(enddt) <= 0){
			out.println("<tr><td>"+flightid+"</td>");
			out.println("<td>"+startct+"</td>");
			out.println("<td>"+destct+"</td>");
			out.println("<td>"+price+"</td></tr>");
         	}}
        } catch (Exception e) {}
		
		out.println("</html");
		out.close();
	}
}

