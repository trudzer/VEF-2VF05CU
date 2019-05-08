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

<form method='post' action='/new_post' accept-charset="UTF-8">
    <textarea = name'postur' cols="100" rows="5"></textarea>
    <p>
        Notendanafn (username): <input type="text" name="userID">
    </p><p>
        <input type='submit' value='skrá póst'>
        </p>
</form>
<hr>

{% if session['logged_in'] %}
    <h3>Breyta eigin póstum</h3>
    <form method='post' action='/change'>
        <input input type='hidden' name="userID" value="{{ user }}">
        <input type='submit' value='Breyta'>
    </form>
{% endif %}

<h4>Þetta er opin vefsíða</h4>
{% endblock %}
