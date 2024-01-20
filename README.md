<h1 align="center">StiebAPI</h1>

![Header Image][header]

> Refer to [Page-Designs][page-design] files (plain html files with linked css) to preview each and every page designed without having to run it.

![shield_general]
[Route Overview][routes.md] - [Function Overview][functions.md] - [Error Codes][errors.md] - [Release Draft][ReleaseDraft]

![shields_dev]
[Security Measurements][security.md] - [Changelog][changelog.md] - [ToDo List][todo.md]

## ![shield_important] ![yellow_sq] `Library Documentation Links` ![yellow_sq] ![shield_important]

> - [Flask-BCrypt][flaskbcrypt_docs]
> - [Flask-Login][flasklogin_docs]
> - [Flask-Mail][flaskmail_docs]
> - [Flask-Security][flasksecurity_docs]
> - [Flask-SQLAlchemy][sqlalchemy_docs]
> - [Flask-WTF][flaskwtf_docs]
> - [Flask-Limiter][flasklimiter_docs]
> - [Flask-Minify][flaskminify_docs]
> - [Flask-Jinja2][jinja2_docs]
> - etc..

## ![shield_critical] ![red_sq] `Security Checklist` ![red_sq] ![shield_critical]

> __Warning__ Always deactivate DEBUG under run.py!

> __Note__ Always check [Security Measurements][security.md] before deploying.

- [ ] Jinja2: [Enable Autoescaping of all inputs][jinja2_docs]
- [X] Flask-WTF: [Enable CSRF-Protection][flaskwtf_docs] - [What is CSRF?][csrf_explanation]
- [ ] For fileuploads, always rename them strictly. [Information][file_uploads]
- [ ] [HTTP-Header Good Practice][http_headers_howto] - [HTTP-Header Documentation][http_headers_docs] - [HTTP-Header List][http_headers_list]
- [ ] [SQLAlchemy Documentation][sqlalchemy_docs] - Always use [ORM-Model objects][sqlalchemy_orm] to describe a query. never use raw SQL. 
- [ ] Use [Flask-Security][flasksecurity_docs] correctly!
- [ ] [Flask Documentation: Security Considerations][flask_docs_security]
- [ ] Only run the Flask app in PRODUCTION behind a reverse proxy like nginx with HTTPS enabled!!!!!!!!!!!!!!!!!
- [ ] [OWASP Top10 Vulnerabilities][top10_vulns]

>To use shields like
![shield_critical][shield_critical] ![shield_info][shield_info] ![shield_success][shield_success] just go ahed and include a link to
https://img.shields.io/badge/-[Text]-[style], for example https://img.shields.io/badge/-CRITICAL-critical

[//]: # (General Link References)

[header]: development/readme_header.png
[page-design]: development/page-designs
[req_txt]: requirements.txt
[blue_sq]: https://placehold.co/15x15/1589F0/1589F0.png
[yellow_sq]: https://placehold.co/15x15/c5f015/c5f015.png
[red_sq]: https://placehold.co/15x15/f03c15/f03c15.png

[//]: # (Relative Documentation Link References)

[routes.md]: development/docs/ROUTES.md
[functions.md]: development/docs/FUNCTIONS.md
[errors.md]: development/docs/ERR_CODES.md
[security.md]: development/docs/SECURITY.md
[changelog.md]: development/docs/CHANGELOG.md
[todo.md]: development/docs/TODO.md

[//]: # (General Documentation Link References)

[ReleaseDraft]: https://github.com/JulianStiebler/PythonFlask_StiebAPI/releases
[flask_docs_security]: https://flask.palletsprojects.com/en/2.2.x/security/
[jinja2_docs]: https://jinja.palletsprojects.com/en/3.1.x/api/
[flaskwtf_docs]: https://flask-wtf.readthedocs.io/en/0.15.x/csrf/
[sqlalchemy_docs]: https://docs.sqlalchemy.org/en/20/
[sqlalchemy_orm]: https://docs.sqlalchemy.org/en/20/orm/
[flasksecurity_docs]: https://pythonhosted.org/Flask-Security/
[http_headers_list]: https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
[http_headers_docs]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
[http_headers_howto]: https://stackoverflow.com/questions/60566143/what-is-the-best-practice-for-changing-headers-in-a-flask-request
[flasklogin_docs]: https://flask-login.readthedocs.io/en/latest/
[flasklimiter_docs]: https://flask-limiter.readthedocs.io/en/stable/
[flaskmigrate_docs]: https://flask-migrate.readthedocs.io/en/latest/
[flaskminify_docs]: https://pypi.org/project/Flask-Minify/
[flaskbcrypt_docs]: https://flask-bcrypt.readthedocs.io/en/1.0.1/
[flaskmail_docs]: https://pythonhosted.org/Flask-Mail/
[flasksecurity_docs]: https://pythonhosted.org/Flask-Security/

[//]: # (Vulnerabilities)

[csrf_explanation]: https://www.synopsys.com/glossary/what-is-csrf.html
[file_uploads]: https://flask.palletsprojects.com/en/1.0.x/patterns/fileuploads/
[top10_vulns]: https://owasp.org/Top10/

[//]: # (Shield Icons)
[shield_critical]: https://img.shields.io/badge/-CRITICAL-critical
[shield_info]: https://img.shields.io/badge/-INFO-informational
[shield_success]: https://img.shields.io/badge/-SUCCESS-success
[shield_important]: https://img.shields.io/badge/-IMPORTANT-yellow
[shield_general]: https://img.shields.io/badge/docs-general-green?logo=appveyor&style=plastic
[shields_dev]: https://img.shields.io/badge/docs-development-green?logo=appveyor&style=plastic
