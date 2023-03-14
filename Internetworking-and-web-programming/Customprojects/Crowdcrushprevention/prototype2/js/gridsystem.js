const container = document.querySelector('#grid');

for (let row = 1; row <= 10; row++) {
  for (let col = 1; col <= 10; col++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.style.gridRow = row;
    cell.style.gridColumn = col;
    container.appendChild(cell);
  }
}