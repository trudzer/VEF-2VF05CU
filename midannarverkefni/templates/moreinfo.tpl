{% extends "base.html" %}

{% block title %}Nánari upplýsingar bensínstöðvar{% endblock %}
{% block content %}
    <h2>Nánari upplýsingar bensínstöðvar</h2>
    {% for item in gogn['results'] %}
        {% if item.key == k %}
            <h3>Söluaðili: {{item.company}}</h3>
            <h3>Staður: {{item.name}}</h3>
            <h3>Verð á 1. lítra af Bensíni, 95 oktan: {{item.bensin95}} kr.</h3>
            <h3>Verð á 1. lítra af dísel olíu: {{item.diesel}} kr.</h3>
        <div class="kort">
            <h4>Staðsetning bensínstövar</h4>
            <ul>
                <li>Breiddargáða: {{item.geo.lat}}</li>
                <li>Lengargráða: {{item.geo.lon}}</li>
                <li><a href="https://www.google.com/maps/@{{item.geo.lat}},{{item.geo.lon}},18z/">Staðsetning á google korti</a> </li>
            </ul>
        </div>
        {% endif %}
    {% endfor %}
{% endblock %}
