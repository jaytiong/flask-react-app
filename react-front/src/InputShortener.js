import { useState } from "react";


const InputShortener = ({setInputValue}) => {
  const [value,setValue] = useState("");
  const [active, setActive] = useState("present");

  return (
    <div className = "inputContainer">
        <h1> URL <span> Shortener</span></h1>
        <div>
        {active === "present" &&
            <input 
              type = "text" 
              placeholder = "Link to Shorten"
              value={value}
              onChange={i =>setValue(i.target.value)}
              />}
        {active === "present" &&
            <button onClick={ async() =>{
              setActive("empty")
              const URL = {"url":value}
              try{
              const response = await fetch('/shorten_url',{
                method:'POST',
                headers:{
                  'Content-type':'application/json',
                  'Accept': 'application/json'
                },
                body: JSON.stringify(URL)
              })

              if (response.ok){
                const res = await response.json()
                const link = res.url
                setInputValue(link);
                setValue("")
                }
              }
              catch{
                console.error('Error')
              }              
            }}>Shorten</button>}
        </div>
    </div> 


  )
}

export default InputShortener