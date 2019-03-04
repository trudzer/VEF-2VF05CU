{% extends "base.html" %}
{% block title %}Staðfesting skráningar {% endblock %}

{% block content %}
    <h3>{{ self.title() }}</h3>
    <table>
        <tr>
            <td>Nafn: </td><th>{{name}}</th>
        </tr>
        <tr>
            <td>Heimilisfang: </td><th> {{home}}</th>
        </tr>
        <tr>
            <td>Netfang: </td><th> {{email}}</th>
        </tr>
        <tr>
            <td>Símanúmer: </td><th> {{phone}}</th>
        </tr>
    </table>
    <h4>Vinnustofa</h4>
    <table>
        <tr>
        {% for item in course %}
        <tr>
            <td>Vinnustofa: </td><th>{{item}}</th>
        </tr>
        {% endfor %}
        </tr>
        <td>Hádegisverður: </td><th>{{food}}</th>
    </table>
    <div class="total">
        <p>Verð án vsk: <b>{{sum}} lr.</b></p>
        <p>Verð með 24% vsk: <b>{{total}} kr.</b></p>
    </div>
{% endblock %}
