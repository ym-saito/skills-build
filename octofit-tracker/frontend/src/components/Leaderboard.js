import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Leaderboard API:', apiUrl);
        console.log('Leaderboard data:', data);
        setLeaderboard(data.results || data);
      });
  }, [apiUrl]);

  return (
    <div className="card mb-4">
      <div className="card-header bg-success text-white">
        <h2 className="h4">Leaderboard</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-bordered">
          <thead className="table-light">
            <tr>
              <th>Team</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.map((item, idx) => (
              <tr key={idx}>
                <td>{item.team}</td>
                <td>{item.points}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="btn btn-success" onClick={() => window.location.reload()}>Reload</button>
      </div>
    </div>
  );
};

export default Leaderboard;
