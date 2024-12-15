import mysql.connector
from datetime import datetime

class StudentManagementSystemCLI:
    def __init__(self):
        # Connect to the database
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root", # replace with the appropriate user
                password="admin", # replace with the appropriate user password
                database="project", # replace with name of the database
                auth_plugin="mysql_native_password"
            )
            self.cursor = self.db.cursor(buffered=True)
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            exit()
        
        self.current_role = None

    def authenticate(self):
        """Authenticate the user based on role."""
        print("Login:")
        username = input("Enter username: ").strip().lower()
        password = input("Enter password: ").strip()

        if username == "admin" and password == "admin":
            self.current_role = "admin"
        elif username == "teacher" and password == "teacher":
            self.current_role = "teacher"
        elif username == "student" and password == "student":
            self.current_role = "student"
        else:
            print("Invalid credentials! Exiting.")
            exit()

    def log_operation(self, operation_type, table_name):
        """Log operations into the operation_logs table."""
        user_role = self.current_role.capitalize()
        operation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""
            INSERT INTO operation_logs (operation_type, table_name, user_role, operation_time)
            VALUES (%s, %s, %s, %s)
        """, (operation_type, table_name, user_role, operation_time))
        self.db.commit()

    def get_fields_for_table(self):
        """Return the fields for the selected table."""
        if self.table == "students":
            return ["sid", "name", "age", "phone", "department", "yearofstudy", "cgpa", "attendancepercentage"]
        else:
            return ["tid", "name", "phone", "department", "yearsofexperience"]

    def show_operations(self):
        """Show operations based on the current role."""
        if self.current_role == "admin":
            operations = ["Create", "Read", "Update", "Delete"]
            tables = ["students", "teachers"]
        elif self.current_role == "teacher":
            operations = ["Create", "Read", "Update","Delete"]
            tables = ["students"]
        else:  # student
            operations = ["Read"]
            tables = ["students"]

        while True:
            print(f"\nSelect table:")
            for i, table in enumerate(tables, 1):
                print(f"{i}. {table.capitalize()}")

            table_choice = int(input("Enter table number: ")) - 1
            self.table = tables[table_choice]

            print(f"\nSelect operation:")
            for i, op in enumerate(operations, 1):
                print(f"{i}. {op}")

            op_choice = int(input("Enter operation number: ")) - 1
            operation = operations[op_choice]

            if operation == "Create":
                self.create_record()
            elif operation == "Read":
                self.read_records()
            elif operation == "Update":
                self.update_record()
            elif operation == "Delete":
                self.delete_record()

            continue_choice = input("\nDo you want to perform another operation? (y/n): ").strip().lower()
            if continue_choice != 'y':
                break

    def create_record(self):
        """Create a record in the selected table."""
        print(f"\nCreating record in {self.table.capitalize()} table")

        fields = self.get_fields_for_table()
        values = []

        for field in fields:
            value = input(f"Enter {field.capitalize()}: ")
            values.append(value)

        try:
            # Validate numeric fields
            if self.table == "students":
                values[0] = int(values[0])  # sid
                values[2] = int(values[2])  # age
                values[5] = int(values[5])  # yearofstudy
                values[6] = float(values[6])  # cgpa
                values[7] = float(values[7])  # attendance
            else:
                values[0] = int(values[0])  # tid
                values[4] = int(values[4])  # yearsofexperience
        except ValueError:
            print("Invalid input type. Please enter the correct type (e.g., number for age, cgpa, etc.)")
            return

        query = f"INSERT INTO {self.table} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(values))})"
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            self.log_operation("Create", self.table)
            print(f"Record created successfully in {self.table.capitalize()} table.")
        except mysql.connector.Error as err:
            print(f"Error creating record: {err}")

    def read_records(self):
        """Read records from the selected table and display column labels."""
        print(f"\nReading records from {self.table.capitalize()} table")

        # Fetch column names for the table
        fields = self.get_fields_for_table()

        # Print column names as labels
        print(", ".join([field.capitalize() for field in fields]))

        # Fetch all records from the table
        query = f"SELECT * FROM {self.table}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        if not records:
            print(f"No records found in {self.table.capitalize()} table.")
        else:
            # Print each record
            for record in records:
                print(record)

        self.log_operation("Read", self.table)



    def update_record(self):
        """Update a record in the selected table."""
        print(f"\nUpdating record in {self.table.capitalize()} table")
        record_id = input(f"Enter the {self.table[0]}id to update: ")

        fields = self.get_fields_for_table()
        values = []

        for field in fields:
            value = input(f"Enter new value for {field.capitalize()}: ")
            values.append(value)

        try:
            if self.table == "students":
                values[0] = int(values[0])  # sid
                values[2] = int(values[2])  # age
                values[5] = int(values[5])  # yearofstudy
                values[6] = float(values[6])  # cgpa
                values[7] = float(values[7])  # attendance
            else:
                values[0] = int(values[0])  # tid
                values[4] = int(values[4])  # yearsofexperience
        except ValueError:
            print("Invalid input type. Please enter the correct type (e.g., number for age, cgpa, etc.)")
            return

        query = f"UPDATE {self.table} SET " + ", ".join([f"{field} = %s" for field in fields]) + f" WHERE {fields[0]} = %s"
        try:
            self.cursor.execute(query, (*values, record_id))
            self.db.commit()
            self.log_operation("Update", self.table)
            print(f"Record with {self.table[0]}id {record_id} updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error updating record: {err}")

    def delete_record(self):
        """Delete a record from the selected table."""
        print(f"\nDeleting record from {self.table.capitalize()} table")
        record_id = input(f"Enter the {self.table[0]}id to delete: ")

        query = f"DELETE FROM {self.table} WHERE {self.table[0]}id = %s"
        try:
            self.cursor.execute(query, (record_id,))
            self.db.commit()
            self.log_operation("Delete", self.table)
            print(f"Record with {self.table[0]}id {record_id} deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error deleting record: {err}")

    def run(self):
        """Main program flow."""
        self.authenticate()
        self.show_operations()

if __name__ == "__main__":
    app = StudentManagementSystemCLI()
    app.run()
