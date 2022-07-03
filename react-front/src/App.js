import './App.css';
import { useState } from 'react';
import InputShortener from './InputShortener';
import Result from './Result';

function App() {
    const [inputValue, setInputValue] = useState("");

  return (
    <div className="App">
      <InputShortener setInputValue={setInputValue}/>
      <Result inputValue={inputValue}/>
    </div>
  );
}

export default App;
