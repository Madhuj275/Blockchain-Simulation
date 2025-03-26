import React from 'react';
import axios from 'axios';

const Blockchain = ({ chain, onTamper }) => {
  const handleTamper = async (index) => {
    const newTransactions = prompt('Enter new transactions (comma separated):');
    if (newTransactions) {
      await axios.post(`/api/tamper/${index}/`, {
        transactions: newTransactions.split(',')
      });
      onTamper();
    }
  };

  return (
    <div className="blockchain">
      {chain.map(block => (
        <div key={block.index} className="block">
          <h3>Block #{block.index}</h3>
          <p><strong>Transactions:</strong> {block.transactions.join(', ')}</p>
          <p><strong>Previous Hash:</strong> {block.previous_hash}</p>
          <p><strong>Hash:</strong> {block.hash}</p>
          <p><strong>Nonce:</strong> {block.nonce}</p>
          {block.index > 0 && (
            <button 
              className="tamper-button"
              onClick={() => handleTamper(block.index)}
            >
              Tamper Block
            </button>
          )}
        </div>
      ))}
    </div>
  );
};

export default Blockchain;