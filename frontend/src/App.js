import React, { useEffect, useState } from "react";

function App() {
  const [rules, setRules] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/rules")
      .then(res => res.json())
      .then(data => setRules(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Market Basket Analysis</h1>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>If Customer Buys</th>
            <th>Then Likely Buys</th>
            <th>Support</th>
            <th>Confidence</th>
            <th>Lift</th>
          </tr>
        </thead>

        <tbody>
          {rules.map((rule, index) => (
            <tr key={index}>
              <td>{rule.antecedents}</td>
              <td>{rule.consequents}</td>
              <td>{rule.support}</td>
              <td>{rule.confidence}</td>
              <td>{rule.lift}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;