const express = require('express');
const dotenv = require('dotenv');
const db = require('./src/config/db');
const employeeController = require('./src/api/employeeController');
const departmentController = require('./src/api/departmentController');

dotenv.config();

const app = express();
app.use(express.json());

// Test database connection
db.getConnection()
    .then(() => {
        console.log('✅ Successfully connected to the database! 💻📡');
    })
    .catch((err) => {
        console.error('❌ Database connection failed: 🔴', err);
    });

// Root route
app.get('/', (req, res) => {
    res.send('🎉🎊 Welcome to the **Employee Management System** API! 🚀🌟 Empowering **teams** 💼🧑‍💻 with **innovative solutions** 🔑📈. Let\'s **build the future** together! 🚀💡');
});

// Register routes
app.use('/api/employees', employeeController);
app.use('/api/departments', departmentController);

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}! 🌟🎉`);
});
