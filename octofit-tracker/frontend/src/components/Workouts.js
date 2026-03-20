import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [data, setData] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Fetched data:', results);
      })
      .catch(err => console.error('Fetch error:', err));
  }, [endpoint]);

  return (
    <div className="card">
      <div className="card-body">
        <h2 className="card-title heading">Workouts</h2>
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-primary">
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Type</th>
                <th>Duration</th>
                <th>Calories</th>
              </tr>
            </thead>
            <tbody>
              {data.length === 0 ? (
                <tr><td colSpan="5" className="text-center">No workouts found.</td></tr>
              ) : (
                data.map((item, idx) => (
                  <tr key={item.id || idx}>
                    <td>{item.id || idx + 1}</td>
                    <td>{item.name || '-'}</td>
                    <td>{item.type || '-'}</td>
                    <td>{item.duration || '-'}</td>
                    <td>{item.calories || '-'}</td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
