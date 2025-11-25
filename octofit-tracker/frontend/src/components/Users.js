import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Users API:', apiUrl);
        console.log('Users data:', data);
        setUsers(data.results || data);
      });
  }, [apiUrl]);

  return (
    <div className="card mb-4">
      <div className="card-header bg-secondary text-white">
        <h2 className="h4">Users</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-bordered">
          <thead className="table-light">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Team</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user, idx) => (
              <tr key={idx}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.team}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <button className="btn btn-secondary" onClick={() => window.location.reload()}>Reload</button>
      </div>
    </div>
  );
};

export default Users;
