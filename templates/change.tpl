{% extends "base.html" %}
{% block title %}Skráir notendur{% endblock %}

{% block content %}
<h3>{{ self.title() }}</h3>
{% with message = get_flashed_message() %}
    {% if message %}
        <h4 class="error">
        {% for message in messages %}
            {{messages}}
        {% endfor %}
        </h4>
    {% endif %}
{% endwith %}

<table>
    <th>Númer</th>
    <th>Póstur</th>
    <th>Notandi</th>
   </tr>

{% for row in userDetails %}
    <tr>
        <td><a href='/changePost/{{row[0]}}'>{{row[0]}}<a></td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
    </tr>
{% endfor %}

</table>

<h5>
    {% if session['logged_in'] %}
        Notandi er skráður
    {% endif %}
</h5>
<p><a href="/logout" class="butt">Útskráning</a></p>
{% endblock %}
