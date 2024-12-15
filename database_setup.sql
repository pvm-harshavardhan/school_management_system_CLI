-- Creating the teachers table
CREATE TABLE teachers (
    tid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    yearsOfExperience INT NOT NULL
);

-- Creating the students table
CREATE TABLE students (
    sid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    yearOfStudy INT NOT NULL,
    cgpa DECIMAL(3, 2) NOT NULL,
    attendancePercentage DECIMAL(5, 2) NOT NULL
);

-- Creating the operation_logs table
CREATE TABLE operation_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    operation_type VARCHAR(50) NOT NULL,
    table_name VARCHAR(50) NOT NULL,
    user_role VARCHAR(50) NOT NULL,
    operation_time DATETIME NOT NULL
);

-- Insert data into the teachers table
INSERT INTO teachers (name, phone, department, yearsOfExperience)
VALUES
    ('Rajesh Sharma', '9876543210', 'CSE', 15),
    ('Sunita Verma', '9876543211', 'ECE', 10),
    ('Anil Kumar', '9876543212', 'EEE', 12),
    ('Pooja Reddy', '9876543213', 'CVL', 8),
    ('Suresh Iyer', '9876543214', 'CSE', 7),
    ('Meena Krishnan', '9876543215', 'ECE', 12),
    ('Vikram Joshi', '9876543216', 'EEE', 18),
    ('Nandini Menon', '9876543217', 'CVL', 9),
    ('Amitabh Das', '9876543218', 'CSE', 20),
    ('Ritika Sharma', '9876543219', 'ECE', 5),
    ('Ramesh Chandra', '9876543220', 'EEE', 14),
    ('Anjali Deshpande', '9876543221', 'CVL', 11);

-- Insert data into the students table
INSERT INTO students (name, age, phone, department, yearOfStudy, cgpa, attendancePercentage)
VALUES
    ('Aarav Gupta', 19, '9876543100', 'CSE', 2, 8.7, 85.5),
    ('Ishita Patel', 20, '9876543101', 'ECE', 3, 8.5, 88.0),
    ('Karan Mehra', 18, '9876543102', 'EEE', 1, 8.2, 90.0),
    ('Ananya Sharma', 21, '9876543103', 'CVL', 4, 8.9, 82.0),
    ('Aryan Singh', 19, '9876543104', 'CSE', 2, 8.6, 87.0),
    ('Priya Mishra', 20, '9876543105', 'ECE', 3, 8.4, 89.5),
    ('Rahul Yadav', 18, '9876543106', 'EEE', 1, 8.3, 92.0),
    ('Neha Desai', 21, '9876543107', 'CVL', 4, 8.8, 83.0),
    ('Vishal Khanna', 20, '9876543108', 'CSE', 3, 8.1, 86.5),
    ('Tanvi Kapoor', 18, '9876543109', 'ECE', 1, 8.0, 89.0),
    ('Rohan Nair', 19, '9876543110', 'EEE', 2, 8.4, 88.5),
    ('Shreya Jaiswal', 21, '9876543111', 'CVL', 4, 8.7, 84.0),
    ('Nikhil Raj', 19, '9876543112', 'CSE', 2, 8.9, 90.0),
    ('Mitali Ghosh', 20, '9876543113', 'ECE', 3, 8.6, 88.7),
    ('Akash Dubey', 18, '9876543114', 'EEE', 1, 8.3, 91.0),
    ('Simran Kaur', 21, '9876543115', 'CVL', 4, 8.5, 83.5),
    ('Arjun Rao', 20, '9876543116', 'CSE', 3, 8.8, 87.0),
    ('Pooja Nair', 19, '9876543117', 'ECE', 2, 8.5, 88.0),
    ('Harsh Vardhan', 18, '9876543118', 'EEE', 1, 8.2, 90.0),
    ('Isha Pathak', 21, '9876543119', 'CVL', 4, 8.6, 84.5),
    ('Aditya Pillai', 20, '9876543120', 'CSE', 3, 8.7, 89.0),
    ('Priyanshi Gupta', 19, '9876543121', 'ECE', 2, 8.4, 87.5),
    ('Manoj Kumar', 18, '9876543122', 'EEE', 1, 8.1, 92.0),
    ('Sneha Agarwal', 21, '9876543123', 'CVL', 4, 8.9, 85.0);