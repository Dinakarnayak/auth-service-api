const db = require('../config/db');

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
