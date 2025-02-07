import os
import zipfile

# Define project directory
project_dir = zip_file_path = r'C:\Users\Admin\Downloads\New folder'

# Create the directory structure
os.makedirs(os.path.join(project_dir, 'src/api'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/config'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/models'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/services'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/utils'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/validators'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/middleware'), exist_ok=True)
os.makedirs(os.path.join(project_dir, 'src/subscribers'), exist_ok=True)

# Files to create in their respective directories
files = {
    'src/api/employeeController.js': '''const express = require('express');
const router = express.Router();
const employeeService = require('../services/employeeService');
const employeeValidator = require('../validators/employeeValidator');

// Create employee
router.post('/create', employeeValidator.createEmployee, async (req, res) => {
    try {
        // Data received from the request body
        const { name, position, salary, email, department, date_of_joining } = req.body;
        
        // Instantiate DTO to ensure structured data
        const employeeDTO = { name, position, salary, email, department, date_of_joining };

        const employee = await employeeService.createEmployee(employeeDTO);
        res.status(201).json({ success: true, data: employee });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
});

// Get all employees
router.get('/', async (req, res) => {
    try {
        const employees = await employeeService.getAllEmployees();
        res.status(200).json({ success: true, data: employees });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
});

module.exports = router;
''',

    'src/api/departmentController.js': '''const express = require('express');
const router = express.Router();
const departmentService = require('../services/departmentService');

// Create department
router.post('/create', async (req, res) => {
    try {
        const { name, description } = req.body;
        const departmentDTO = { name, description };
        
        const department = await departmentService.createDepartment(departmentDTO);
        res.status(201).json({ success: true, data: department });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
});

// Get all departments
router.get('/', async (req, res) => {
    try {
        const departments = await departmentService.getAllDepartments();
        res.status(200).json({ success: true, data: departments });
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
});

module.exports = router;
''',

    'src/config/db.js': '''const mysql = require('mysql2');
const config = require('./config');

// Create MySQL connection pool
const pool = mysql.createPool({
    host: config.DB_HOST,
    user: config.DB_USER,
    password: config.DB_PASSWORD,
    database: config.DB_NAME
});

// Promise wrapper for the pool to use async/await
const promisePool = pool.promise();

module.exports = promisePool;
''',

    'src/config/config.js': '''require('dotenv').config();

module.exports = {
    PORT: process.env.PORT || 5000,
    DB_HOST: process.env.DB_HOST,
    DB_USER: process.env.DB_USER,
    DB_PASSWORD: process.env.DB_PASSWORD,
    DB_NAME: process.env.DB_NAME,
    JWT_SECRET: process.env.JWT_SECRET
};
''',

    'src/services/employeeService.js': '''const db = require('../config/db');

// Employee DTO class
class EmployeeDTO {
    constructor(name, position, salary, email, department, date_of_joining) {
        this.name = name;
        this.position = position;
        this.salary = salary;
        this.email = email;
        this.department = department;
        this.date_of_joining = date_of_joining;
    }
}

const createEmployee = async (data) => {
    const { name, position, salary, email, department, date_of_joining } = data;

    // Validate and create DTO
    const employeeDTO = new EmployeeDTO(name, position, salary, email, department, date_of_joining);
    
    const query = `
        INSERT INTO Employee (name, position, salary, email, department, date_of_joining)
        VALUES (?, ?, ?, ?, ?, ?)
    `;
    const [result] = await db.execute(query, [employeeDTO.name, employeeDTO.position, employeeDTO.salary, employeeDTO.email, employeeDTO.department, employeeDTO.date_of_joining]);
    
    return { id: result.insertId, ...employeeDTO };
};

const getAllEmployees = async () => {
    const query = 'SELECT * FROM Employee';
    const [employees] = await db.execute(query);
    return employees;
};

module.exports = {
    createEmployee,
    getAllEmployees
};
''',

    'src/services/departmentService.js': '''const db = require('../config/db');

// Department DTO class
class DepartmentDTO {
    constructor(name, description) {
        this.name = name;
        this.description = description;
    }
}

const createDepartment = async (data) => {
    const { name, description } = data;

    // Create DTO
    const departmentDTO = new DepartmentDTO(name, description);
    
    const query = `
        INSERT INTO Department (name, description)
        VALUES (?, ?)
    `;
    const [result] = await db.execute(query, [departmentDTO.name, departmentDTO.description]);
    
    return { id: result.insertId, ...departmentDTO };
};

const getAllDepartments = async () => {
    const query = 'SELECT * FROM Department';
    const [departments] = await db.execute(query);
    return departments;
};

module.exports = {
    createDepartment,
    getAllDepartments
};
''',

    'src/utils/logger.js': '''const winston = require('winston');

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
    ),
    transports: [
        new winston.transports.Console()
    ]
});

module.exports = logger;
''',

    'src/validators/employeeValidator.js': '''const { check, validationResult } = require('express-validator');

const createEmployee = [
    check('name').notEmpty().withMessage('Name is required'),
    check('position').notEmpty().withMessage('Position is required'),
    check('salary').optional().isFloat().withMessage('Salary must be a number'),
    check('email').optional().isEmail().withMessage('Invalid email format'),
    check('department').optional().notEmpty().withMessage('Department is required'),
    check('date_of_joining').optional().isDate().withMessage('Invalid date of joining'),

    (req, res, next) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ success: false, errors: errors.array() });
        }
        next();
    }
];

module.exports = {
    createEmployee
};
''',

    'src/middleware/authMiddleware.js': '''const jwt = require('jsonwebtoken');
const config = require('../config/config');

const authMiddleware = (req, res, next) => {
    const token = req.header('Authorization')?.split(' ')[1];
    if (!token) return res.status(401).json({ success: false, message: 'Access denied' });

    try {
        const decoded = jwt.verify(token, config.JWT_SECRET);
        req.user = decoded;
        next();
    } catch (error) {
        res.status(400).json({ success: false, message: 'Invalid token' });
    }
};

module.exports = authMiddleware;
''',

    'src/subscribers/eventSubscriber.js': '''const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

// Example: subscribe to employee creation event
eventEmitter.on('employeeCreated', (employee) => {
    console.log('Employee created:', employee);
    // Additional actions like sending notifications can be added here
});

module.exports = eventEmitter;
''',

    'server.js': '''const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./src/config/db');
const employeeController = require('./src/api/employeeController');
const departmentController = require('./src/api/departmentController');
const authMiddleware = require('./src/middleware/authMiddleware');

dotenv.config();

// Connect to DB (MySQL)
connectDB();

const app = express();
app.use(express.json());

// API Routes
app.use('/api/employees', employeeController);
app.use('/api/departments', departmentController);

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
''',

    'package.json': '''{
  "name": "employee_management_system",
  "version": "1.0.0",
  "description": "Employee Management System",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "mysql2": "^2.3.3",
    "dotenv": "^8.2.0",
    "express-validator": "^6.8.0",
    "jsonwebtoken": "^8.5.1",
    "winston": "^3.2.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.6"
  },
  "author": "",
  "license": "ISC"
}
''',

    '.env': '''PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=employee_management
JWT_SECRET=your_jwt_secret
'''
}

# Create files in their respective directories
for file_path, content in files.items():
    with open(os.path.join(project_dir, file_path), 'w') as f:
        f.write(content)

# Create a ZIP file of the project folder # Make sure this path is correct
zip_file_path = r'C:\Users\Admin\Downloads\New folder\employee_management_system.zip'

# Create a zip file of the project directory
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_dir))

print(f"Zip file created at: {zip_file_path}")

