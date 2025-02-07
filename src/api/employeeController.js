const express = require('express');
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
