import React, { useState } from 'react';

function CounterApp() {
  let count = 0; 

  function increment() {
    count += 1; 
    console.log("Count:", count); 
  }

  return (
    <div>
      <h1>Counter App</h1>
      <p>Count: {count}</p> 
      <button onClick={increment}>Increment</button>
    </div>
  );
}

export default CounterApp;
