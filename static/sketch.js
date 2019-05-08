const CANVAS_WIDTH = 540;
const STROKE_WEIGHT = 58;

function setup() {
  canvas = createCanvas(CANVAS_WIDTH, CANVAS_WIDTH);
  background(0);
  var canvas_x_pos = (windowWidth - width) / 2;
  var canvas_y_pos = (windowHeight - height - 100) / 2;
  canvas.position(canvas_x_pos, canvas_y_pos);

  let predictButton = select('#predict');

  $(function() {
    $('#predict').bind('click', function() {
      var pixels = getPixels();
      $.getJSON($SCRIPT_ROOT + '/_predict', {
        pixels: pixels.toString()
      }, function(data) {
        $("#prediction").text(data.result);
      });
      return false;
    });
  });

  predictButton.position(canvas_x_pos, canvas_y_pos + height + 20);

  let clearButton = select('#clear');
  clearButton.mousePressed(function() {
    clear();
  });
  clearButton.position(canvas_x_pos + width - clearButton.width + 10, canvas_y_pos + height + 20);

  let prediction = select('#prediction');
  prediction.position(predictButton.x, predictButton.y + predictButton.height + 10);
}

function draw() {
  strokeWeight(STROKE_WEIGHT);
  stroke(255);
  if (mouseIsPressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
  }
}

function getPixels() {
  let img = get();
  img.resize(28, 28);
  img.loadPixels();
  return img.pixels;
}
