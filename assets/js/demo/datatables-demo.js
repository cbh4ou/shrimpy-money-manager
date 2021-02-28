// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    "ordering": true,
    "processing": true,
    "ajax": "/funnel/stats/table",
    "columnDefs": [
      {
        "targets": [ 1,2,3,4 ],
        "render": function ( data, type, full, meta ) {
        return `$${data}`;
        }
         }
    
 ],
    "columns": [
            { "data": "funnelname",

                "render": function(data, type, row, meta){

                data = '<a href="/funnel/stats/' + row.funnel_id + '" target="_blank">' + data + '</a>';


            return data;
         }
            },
            { "data": "net_epc" },
            { "data": "net_aov" },
            { "data": "epc" },
            { "data": "aov" },
            { "data": null,
              "render": function ( data, type, row ) {
                data= '<a class="btn" href="/funnel/editor/' + row.funnel_id + '" target="_blank" role="button">Edit</a>';
                return data
              }
            }
        ]
})
});
