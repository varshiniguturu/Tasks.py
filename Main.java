import java.sql.*;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        try {

            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/studentdb",
                    "root",
                    "1234");

            while (true) {

                System.out.println("\n===== STUDENT MANAGEMENT SYSTEM =====");
                System.out.println("1. Add Student");
                System.out.println("2. View Students");
                System.out.println("3. Delete Student");
                System.out.println("4. Exit");

                System.out.print("Enter your choice: ");

                int choice = sc.nextInt();

                switch (choice) {

                    case 1:

                        System.out.print("Enter Student ID: ");
                        int id = sc.nextInt();
                        sc.nextLine();

                        System.out.print("Enter Student Name: ");
                        String name = sc.nextLine();

                        System.out.print("Enter Department: ");
                        String dept = sc.nextLine();

                        System.out.print("Enter Marks: ");
                        int marks = sc.nextInt();

                        String insertQuery =
                                "INSERT INTO students VALUES (?, ?, ?, ?)";

                        PreparedStatement pst =
                                con.prepareStatement(insertQuery);

                        pst.setInt(1, id);
                        pst.setString(2, name);
                        pst.setString(3, dept);
                        pst.setInt(4, marks);

                        pst.executeUpdate();

                        System.out.println("Student Added Successfully!");

                        break;

                    case 2:

                        String viewQuery = "SELECT * FROM students";

                        PreparedStatement viewPst =
                                con.prepareStatement(viewQuery);

                        ResultSet rs = viewPst.executeQuery();

                        System.out.println("\n===== STUDENT RECORDS =====");

                        while (rs.next()) {

                            System.out.println(
                                    rs.getInt("id") + " | " +
                                    rs.getString("name") + " | " +
                                    rs.getString("department") + " | " +
                                    rs.getInt("marks"));
                        }

                        break;

                    case 3:

                        System.out.print("Enter Student ID to Delete: ");

                        int deleteId = sc.nextInt();

                        String deleteQuery =
                                "DELETE FROM students WHERE id=?";

                        PreparedStatement deletePst =
                                con.prepareStatement(deleteQuery);

                        deletePst.setInt(1, deleteId);

                        deletePst.executeUpdate();

                        System.out.println("Student Deleted Successfully!");

                        break;

                    case 4:

                        System.out.println("Exiting Program...");
                        con.close();
                        System.exit(0);

                    default:

                        System.out.println("Invalid Choice!");
                }
            }

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}