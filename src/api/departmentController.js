const express = require('express');
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
