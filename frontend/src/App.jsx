import { useState } from "react";
import { queryDB } from "./api";


export default function App() {
const [operation, setOperation] = useState("SELECT");
const [question, setQuestion] = useState("");
const [response, setResponse] = useState(null);


const submit = async (e) => {
e.preventDefault();
const data = await queryDB({ operation, question });
setResponse(data);
};


return (
<div style={{ padding: 30}}>
  <h2>AI SQL SaaS (Ollama)</h2>


  <form onSubmit={submit}>
<h2>AI SQL SaaS (Ollama)</h2>


<form onSubmit={submit}>
  <select value={operation} onChange={e => setOperation(e.target.value)}>
    <option>SELECT</option>
    <option>INSERT</option>
    <option>UPDATE</option>
    <option>DELETE</option>
  </select>
  <br /><br />
  <input
  value={question}
  onChange={e => setQuestion(e.target.value)}
  placeholder="Ask in English"
  style={{ width: 400 }}
 />
 <br /><br />
 <button>Execute</button>
</form>


{response && (
   <div style={{ marginTop: 20 }}>
     <b>Generated SQL</b>
     <pre>{response.sql}</pre>
     <b>Result</b>
     <pre>{JSON.stringify(response.result, null, 2)}</pre>
    </div>
   )}
  </div>
 );
}
  
<option>SELECT</option>
<option>INSERT</option>
<option>UPDATE</option>
<option>DELETE</option>
</select>
<br /><br />
<input
value={question}
onChange={e => setQuestion(e.target.value)}
placeholder="Ask in English"
style={{ width: 400 }}
/>
