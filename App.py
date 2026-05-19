CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT,
    department TEXT,
    semester TEXT
);

CREATE TABLE attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    attendance_percentage INTEGER,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
);

CREATE TABLE notifications (
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    notification_message TEXT,
    notification_date TEXT,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
);

CREATE TABLE assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_name TEXT,
    due_date TEXT,
    assignment_status TEXT,

    FOREIGN KEY (student_id)
    REFERENCES students(student_id)
);

CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT,
    event_date TEXT,
    event_time TEXT
);

INSERT INTO students
(name, email, password, department, semester)

VALUES

('Ali Khan','ali@gmail.com','123','Computer Science','6th'),

('Sara Ahmed','sara@gmail.com','123','Software Engineering','4th'),

('Ahmed Raza','ahmed@gmail.com','123','Information Technology','8th');

INSERT INTO attendance
(student_id, attendance_percentage)

VALUES

(1,68),
(2,93),
(3,72);

INSERT INTO notifications
(student_id, notification_message, notification_date)

VALUES

(1,'Warning! Attendance below 75%','2026-05-17'),

(2,'Assignment submission due tomorrow','2026-05-17'),

(3,'AI workshop scheduled at 2 PM','2026-05-17');

INSERT INTO assignments
(student_id, subject_name, due_date, assignment_status)

VALUES

(1,'Database Systems','2026-05-20','Pending'),

(2,'Software Engineering','2026-05-22','Submitted'),

(3,'Artificial Intelligence','2026-05-18','Pending');

INSERT INTO events
(event_name, event_date, event_time)

VALUES

('Mathematics Seminar','2026-05-19','10:00 AM'),

('Sports Day','2026-05-21','09:00 AM'),

('Parent Teacher Meeting','2026-05-25','02:00 PM');