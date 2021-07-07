import React, { useState, useEffect } from 'react';
import './App.css';


function App() {

const [flag, setFlag] = useState('inactive');

  useEffect(() => {
    let profileUrl = `${process.env.REACT_APP_API}/api`;
    fetch(profileUrl).then(res => res.json()).then(data => {
      setFlag(data.data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
       Welcome to demo
      </header>
      <p> The current system is active with Mango : { flag} </p>
    </div>
  );
}

export default App;
