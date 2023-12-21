// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;



import React from 'react';

function Test() {
  const name = 'John Doe';
  const items = ['Apple', 'Banana', 'Cherry'];

  return (
    <div className='Test'>
      <h1>Hello, {name}!</h1>
      <p className='intro'>This is an introduction paragraph.</p>

      <ul>
        {items.map((item, index) => <li key={index}>{item}</li>)}
      </ul>

      <button onClick={() => { alert('Button is clicked'); }}>
        Click me
      </button>

      <input type='text' placeholder='Enter some text' />

      <img src='https://i.imgur.com/MK3eW3Am.jpg' alt='placeholder'/>
    </div>
  )
}

export default Test;
