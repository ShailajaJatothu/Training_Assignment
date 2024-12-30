create database revision
use revision;
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each employee
    first_name VARCHAR(50) NOT NULL,            -- Employee's first name
    last_name VARCHAR(50) NOT NULL,             -- Employee's last name
    email VARCHAR(100) UNIQUE,                  -- Employee's email address
    phone_number VARCHAR(15),                   -- Employee's phone number
    job_title VARCHAR(50) NOT NULL,             -- Job title (e.g., 'Manager', 'Developer')
    department_id INT,                          -- Foreign key to the 'departments' table
    salary DECIMAL(10, 2) NOT NULL,             -- Employee's salary
    commission_pct DECIMAL(5, 2),               -- Commission percentage (if applicable)
    manager_id INT                           -- Foreign key to another employee (manager)
)
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each department
    department_name VARCHAR(100) NOT NULL,         -- Name of the department
    location VARCHAR(100),                         -- Location of the department
    manager_id INT                              -- Manager for the department (links to employees table)
);
INSERT INTO departments (department_name, location, manager_id)
VALUES 
('Human Resources', 'New York', 1),
('Engineering', 'San Francisco', 2),
('Sales', 'Los Angeles', 3),
('Marketing', 'Chicago', 4),
('Finance', 'Boston', 5),
('IT Support', 'Austin', 6),
('Research and Development', 'Seattle', 7),
('Operations', 'Houston', 8),
('Customer Service', 'Denver', 9),
('Legal', 'Washington DC', 10);

INSERT INTO employees (first_name, last_name, email, phone_number, job_title, department_id, salary, commission_pct, manager_id)
VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', 'HR Manager', 1, 70000, NULL, NULL),
('Jane', 'Smith', 'jane.smith@example.com', '1234567891', 'Software Engineer', 2, 90000, NULL, 2),
('Mike', 'Brown', 'mike.brown@example.com', '1234567892',  'Sales Executive', 3, 60000, 0.10, 3),
('Emily', 'Davis', 'emily.davis@example.com', '1234567893', 'Marketing Specialist', 4, 55000, NULL, 4),
('Robert', 'Wilson', 'robert.wilson@example.com', '1234567894',  'Finance Manager', 5, 80000, NULL, NULL),
('Sophia', 'Moore', 'sophia.moore@example.com', '1234567895',  'IT Technician', 6, 45000, NULL, 6),
('James', 'Taylor', 'james.taylor@example.com', '1234567896',  'R&D Scientist', 7, 95000, NULL, 7),
('Olivia', 'Anderson', 'olivia.anderson@example.com', '1234567897',  'Operations Supervisor', 8, 60000, NULL, 8),
('William', 'Jones', 'william.jones@example.com', '1234567898', 'Customer Support Rep', 9, 40000, NULL, 9),
('Emma', 'Garcia', 'emma.garcia@example.com', '1234567899',  'Legal Advisor', 10, 75000, NULL, 10);
select * from employees;
select * from departments;


select name,last_name,location from employees join departments on employees.manager_id=departments.manager_id;


select sum(salary) from employees;
select employee_id,first_name,last_name
from employees where salary>500000 
group by department_id 
order by department_id;

SELECT department_id, SUM(salary) AS total_salary
FROM employees
WHERE salary > 1000
GROUP BY department_id;


select count(department_id) from employees;


select avg(salary) from employees;

select employee_id,first_name,last_name from employees where salary between 20000 and 50000;

select employee_id,first_name,last_name from employees where salary in(20000,50000);

select * from employees;

select employee_id,first_name,last_name from employees where first_name like 'j%';

select employee_id,first_name,last_name from employees where first_name like '_m%';

select employee_id,first_name,last_name from employees where first_name like '%a';

select min(salary) as minimum,max(salary) as maximum from employees;

delete from employees where first_name='Jane';

set sql_safe_updates=0;

update employees set salary=100000 where employee_id=4;

select employee_id,first_name,last_name from employees order by salary limit 3;


alter table employees add column surname varchar(20);

alter table employees rename column first_name to name;

alter table employees drop column surname;

