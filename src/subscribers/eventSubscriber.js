const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

// Example: subscribe to employee creation event
eventEmitter.on('employeeCreated', (employee) => {
    console.log('Employee created:', employee);
    // Additional actions like sending notifications can be added here
});

module.exports = eventEmitter;
