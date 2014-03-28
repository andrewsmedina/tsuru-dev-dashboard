$(function () {
    $("div.metric div.sparkline").each(function (index, elem) {
        var e = $(elem);
        var value_element = e.parent().find('p.value a');
        var timestamp_element = e.parent().find('span.timestamp');
        var original_value = value_element.html();
        
        var url = "/metric/" + e.data('metric') + ".json";
        $.getJSON(url, function(response) {
            // flot time series data needs to be in *milliseconds*, not seconds.
            // fixing this in Python would be easier but would limit reuse.
            for (var i=0; i < response.data.length; i++) {
                response.data[i][0] = response.data[i][0] * 1000;
            };
            var options = {
                xaxis: {show: false, mode: "time"},
                yaxis: {show: false, min: 0},
                grid: {borderWidth: 0, hoverable: true},
                colors: ["yellow"]
            };
            if (response.period == 'daily') {
                options.bars = {
                    show: true,
                    barWidth: 24 * 60 * 60 * 1000,
                    fillColor: "yellow",
                    lineWidth: 1,
                    align: "center",
                };
            } else if (response.period == 'weekly') {
                options.bars = {
                    show: true,
                    barWidth: 24 * 60 * 60 * 7 * 1000,
                    fillColor: "yellow",
                    lineWidth: 1,
                    align: "center",
                };
            }
            $.plot(e, [response.data], options);
            
            e.bind('plothover', function(event, pos, item) {
                if (item) {
                    value_element.html(item.datapoint[1]);
                    var d = dddash.format_timestamp(item.datapoint[0], response.period);
                    timestamp_element.html(d);
                } else {
                    value_element.html(original_value);
                    timestamp_element.html('&nbsp;');
                }
            });
        });
        
        e.click(function() {
            window.location = "/metric/" + e.data('metric') + '/';
        })
    });
});