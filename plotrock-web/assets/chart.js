// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});


function drawSensitivity() {
    var jsonData = $.ajax(
    {
        url: "/alg/sensitivity",
        dataType: "json",
        async: false
      }).responseText;

    // Create our data table out of JSON data loaded from server.
    var data = new google.visualization.DataTable(jsonData);

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    chart.draw(data, {width: 400, height: 240});
}