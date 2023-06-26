
let currentInput = '';
let previousInput = '';
let operator = '';
let functionSelected = '';

function appendNumber(number) {
  currentInput += number;
  updateResult();
}

function appendOperator(op) {
  operator = op;
  previousInput = currentInput;
  currentInput = '';
  updateResult();
}

function clearInput() {
  currentInput = '';
  previousInput = '';
  operator = '';
  functionSelected = '';
  updateResult();
}

function calculateResult() {
    let result;
    const num1 = parseFloat(previousInput);
    const num2 = parseFloat(currentInput);
  
    if (operator === '+') {
      result = num1 + num2;
      currentInput = `${num1} + ${num2}`;
    } else if (operator === '-') {
      result = num1 - num2;
      currentInput = `${num1} - ${num2}`;
    } else if (operator === '*') {
      result = num1 * num2;
      currentInput = `${num1} * ${num2}`;
    } else if (operator === '/') {
      result = num1 / num2;
      currentInput = `${num1} / ${num2}`;
    } else if (operator === '^') {
      result = Math.pow(num1, num2);
      currentInput = `${num1} ^ ${num2}`;
    }
  
    if (!isNaN(result)) {
      currentInput += ` = ${result}`;
      previousInput = '';
      operator = '';
      updateResult();
    }
  }
  
  
  

function calculateSquareRoot() {
  const num = parseFloat(currentInput);
  if (num >= 0) {
    const result = Math.sqrt(num);
    currentInput = `√(${num})`;
    if (!isNaN(result)) {
      currentInput += ` = ${result}`;
    }
  } else {
    currentInput = 'Invalid input';
  }
  updateResult();
}

function calculateSin() {
  const num = parseFloat(currentInput);
  const result = Math.sin(degToRad(num));
  currentInput = `sin(${num})`;
  if (!isNaN(result)) {
    currentInput += ` = ${result}`;
  }
  updateResult();
}

function calculateCos() {
  const num = parseFloat(currentInput);
  const result = Math.cos(degToRad(num));
  currentInput = `cos(${num})`;
  if (!isNaN(result)) {
    currentInput += ` = ${result}`;
  }
  updateResult();
}

function calculateTan() {
  const num = parseFloat(currentInput);
  if (num === 90) {
    currentInput = `tan(${num}) = Infinity`;
  } else {
    const result = Math.tan(degToRad(num));
    currentInput = `tan(${num})`;
    if (!isNaN(result)) {
      currentInput += ` = ${result}`;
    }
  }
  updateResult();
}

// function calculatePower() {
//   const num1 = parseFloat(currentInput);
//   const num2 = parseFloat(currentInput);
//   const result = Math.pow(num1, num2);
//   currentInput = `${num1} ^ ${num2}`;
//   if (!isNaN(result)) {
//     currentInput += ` = ${result}`;
//   }
//   updateResult();
// }

function degToRad(degrees) {
  return (degrees * Math.PI) / 180;
}

function updateResult() {
  document.getElementById('result').value = currentInput;
}


