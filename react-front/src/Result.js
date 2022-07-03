import { useState} from "react"
import CopyToClipboard from "react-copy-to-clipboard"

function refreshPage() {
  window.location.reload(false);
}

const Result = ({inputValue}) => {
    const [copied, setCopied] = useState(false)
  return (
    <div className ="result">
      <div>
      <a href={inputValue}>{inputValue}</a><br/>
      <CopyToClipboard 
        text={inputValue}
        onCopy={() => setCopied(true)}
        >
      <button className={copied ? "copied" : ""} 
        onClick={refreshPage}>Copy To Clipboard</button> 
      </CopyToClipboard>
      
      </div>
    </div>
  )
}

export default Result