import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Workouts endpoint:', endpoint);
        console.log('Fetched workouts:', data);
        setWorkouts(data.results || data);
      });
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Workouts</h2>
      <table className="table table-success">
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout, idx) => (
            <tr key={idx}>
              <td>{workout.id}</td>
              <td>{workout.type}</td>
              <td>{workout.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Workouts;
