import React, { useState } from 'react';
import axios from 'axios';

const TransactionForm = ({ onTransactionAdded }) => {
  const [transaction, setTransaction] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!transaction.trim()) return;

    try {
      await axios.post('/api/transactions/', {
        transactions: [transaction.trim()]
      });
      setTransaction('');
      onTransactionAdded(); // Refresh the blockchain
    } catch (error) {
      console.error('Error adding transaction:', error);
      alert('Failed to add transaction');
    }
  };

  return (
    <div className="transaction-form">
      <h2>Add Transaction</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={transaction}
          onChange={(e) => setTransaction(e.target.value)}
          placeholder="e.g. Alice sends Bob 5 BTC"
          required
        />
        <button type="submit">Mine Block</button>
      </form>
    </div>
  );
};

export default TransactionForm;