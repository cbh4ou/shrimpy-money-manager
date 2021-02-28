

// JavaScript modules
require('@fortawesome/fontawesome-free');
require('jquery');
require('popper.js');
require('bootstrap');
require('chart.js');
require('datatables.net');
require('datatables.net-bs4');
require('jquery-form');
require('bootstrap-validator');

require.context(
  '../img', // context folder
  true, // include subdirectories
  /.*/, // RegExp
);

// Your own code
require('./demo/datatables-demo.js');
require('./plugins.js');
require('./script.js');
require('./sb-admin-2.js');
require('./sales_pie.js');
