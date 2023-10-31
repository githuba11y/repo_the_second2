
console.log('I did 1');
console.log('I did 2');
console.log('I did 3');

setTimeout(() => {
   throw new Error('I failed');
}, 5000);