<!DOCTYPE html>
<html>
<head>
    <title>Gengi gjaldmipla</title>
    <style>
        body{
			background:#dfefef;
			max-width: 50em;
			margin: 0 auto;
			font-family:Sans-serif;
			}
		.box li{
			{padding: .5em 0}
		.box{
			border:1px dotted;
			border-radius: 5px;
			background-color: #decdcd;
			padding:.5px;}
    </style>
</head>
<body>
<h1>gengi gjaldmiðla</h1>
    <div class="box">
        <ul>
	{% for i in data['results']: %}
	    <li>{{i['longName']}} {{i['shortName']}}, gengi ISKR: {{i['value']}}</li>
	{% endfor %}
        </ul>
    </div>
</body>
</html>
