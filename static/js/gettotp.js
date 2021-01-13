var interval = 30;
var value = 30;

function tick() {
  /* Get and display cyclic timer given time interval. */
  value = Math.floor((Date.now() / 1000) % interval);

  $("#progressLabel").html("Remaining: " + (interval - value - 1));
  $("#progressBar").css("width", 100 * value / interval + "%");

  if ($("#TOTPcode").html() == NaN || $("#TOTPcode").html() == "NaN") {
    console.log("TOTP: retrying...");
    getCode();
  }

  if (value == 0) {
    getCode();
  }
}

function getCode() {
  /* Ask server for a code given a certain hashing algorithm. */
  $.ajax({
    url: "/api/endpoint",
    type: "GET",
    data: {
      'key': $("#key").val(),
      'interval': $("#interval").val(),
      'length': $("#length").val(),
      'algo': $("#algo").val()
    },
    success: function(res) {
      $("#TOTPcode").html(res);
    }
  });
}

$( ".form-control" ).change(function() {
  interval = $("#interval").val();
  getCode();
});

/* Repeat every second. */
setInterval(tick, 1000);
getCode();
