{% extends "base.html" %}
{% block title %}db innskráning{% endblock %}

{% block content %}
{% if error %}
    <p class="error">Villa:<strong>{{error}}</strong>
{% endif %}

<h3>{{self.title()}}</h3>
<form method="POST" action="nyskra">
    <p>Notandanafn <input type="text" name="userID" required></p>
    <p>nafn <input type="text" name="user_name" required></p>
    <p>Tölvupóstur <input type="email" name="user_email" required></p>
    <p>Lykilorð <input type="text" name="user_password" required></p>
    <p><input type="submit" value="senda"></p>
</form>
{% if session['logged_in'] %}
    You're logged in already!
{% else %}
    <h3>Innskráning</h3>
    <form method="POST" action="login">
        <p>Notandanafn <input type="text" name="user_name" required></p>
        <p>Lykilorð <input type="text" name="user_password" required></p>
        <p><input type="submit" value="senda"></p>
    </form>
{% endif %}
<table>
    <tr>
        <th>Póstar frá notendum</th>
    </tr>
    {% for postur in userDetails %}
    <tr>
        <td> {{postur[0]}} </td>
    </tr>
    {% endfor %}
</table>

{% endblock %}
