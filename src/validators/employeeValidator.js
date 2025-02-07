const { check, validationResult } = require('express-validator');

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
