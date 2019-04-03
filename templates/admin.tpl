{% extends "base.html" %}
{% block title %}Skráir notendur{% endblock %}

{% block content %}
<h3>{{ self.title() }}</h3>

<table>
    <tr>
        <th>Nafn</th>
        <th>Email</th>
        <th>password</th>
    </tr>
    {% for user in userDetails %}
    <tr>
        <td> {{user[0]}}</td>
        <td> {{user[1]}}</td>
        <td> {{user[2]}}</td>
    </tr>
    {% endfor %}
</table>

<h4>Þetta er opin vefsíða</h4>
{% endblock %}
