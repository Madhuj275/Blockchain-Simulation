import React, { useState, useEffect } from 'react';
import axios from 'axios';
import TransactionForm from './components/TransactionForm';
import Blockchain from './components/Blockchain';
import './App.css';

function App() {
  const [chain, setChain] = useState([]);
  const [isValid, setIsValid] = useState(true);

  const fetchBlockchain = async () => {
    try {
      const response = await axios.get('/api/chain/');
      setChain(response.data);
      const validation = await axios.get('/api/validate/');
      setIsValid(validation.data.is_valid);
    } catch (error) {
      console.error('Error fetching blockchain:', error);
    }
  };

  useEffect(() => {
    fetchBlockchain();
  }, []);

  return (
    <div className="app">
      <h1>Blockchain Simulator</h1>
      <div className={`status ${isValid ? 'valid' : 'invalid'}`}>
        {isValid ? '✓ Blockchain Valid' : '✗ Blockchain Invalid'}
      </div>
      <TransactionForm onTransactionAdded={fetchBlockchain} />
      <Blockchain chain={chain} onChainUpdated={fetchBlockchain} />
    </div>
  );
}

export default App;