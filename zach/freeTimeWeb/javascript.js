import Chart from 'chart.js/auto'
import { getDimensions } from './api'

(async function() {
  const data = await getDimensions();

  new Chart(
    document.getElementById('acquisitions'),
    {
      type: 'bubble',
      data: {
        labels: data.map(x => x.year),
        datasets: [
          {
            label: 'Dimensions',
            data: data.map(row => ({
              x: row.width,
              y: row.height,
              r: row.count
            }))
          }
        ]
      }
    }
  );
})();
 