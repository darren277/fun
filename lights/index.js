const dic = {"🔴": 'red', "🟠": 'orange', "🟡": 'yellow', "🟣": 'purple', "🟢": 'green', "🔵": 'blue', "⚪": 'white', "⚫": null}

/*
optional alternative:
const pegs = [
  { x: 0, y: 2, color: 'orange' },
  { x: 0, y: 3, color: 'orange' },
];
*/

//console.log('height', pattern.length);
//console.log('width', pattern[0].length);


const pegRadius = 10;

// Distance between peg centers
const cellSize = 30;

function render(pattern){
    clearCanvas();

    const canvas = document.getElementById('liteBriteCanvas');
    const ctx = canvas.getContext('2d');

    console.log('pattern', typeof pattern, pattern.length, typeof pattern[0], pattern[0].length, typeof pattern[0][0], pattern[0][0]);

    for (let row = 0; row < pattern.length; row++) {
        for (let col = 0; col < pattern[row].length; col++) {
            const color = pattern[row][col];
            if (dic[color]) {
                // Calculate where on the canvas to draw
                const x = col * cellSize + cellSize / 2;
                const y = row * cellSize + cellSize / 2;

                // glow effect:
                ctx.shadowBlur = 10;
                ctx.shadowColor = dic[color];

                ctx.beginPath();
                ctx.arc(x, y, pegRadius, 0, Math.PI * 2);
                ctx.fillStyle = dic[color];
                ctx.fill();
            }
        }
    }
}

fetch('/lights/data.json').then(response => response.json()).then(data => {render(data)}).catch(error => console.error('Error:', error));


function clearCanvas(){
    const canvas = document.getElementById('liteBriteCanvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

