const db = require('../config/db');

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
