# `StiebAPI powered by Flask`

> `and multiple extensions:`
>
> - Flask-BCrypt
> - Flask-Login
> - Flask-Mail
> - Flask-Security
> - Flask-SQLAlchemy & SQLAlchemy
> - Flask-WTF & WTForms
> - MarkupSafe
> - etc.. - see [requirements.txt](requirements.txt) for specific versions and other small utilities

## ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `General Resources` ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png)

> - Cheatsheets: [To-Do Cheatsheet](https://github.com/JulianStiebler/PythonFlask_StiebAPI#to-do-list) - [Security Cheatsheet](https://github.com/JulianStiebler/PythonFlask_StiebAPI#security-checklist)
> - App Related: [Routes Overview](development/docs/ROUTES.md) - [Database Model](development/docs/MODEL.md) - [Function Overview](development/docs/FUNCTIONS.md) - [Error Codes](development/docs/ERR_CODES.md) - [Security Measurements](development/docs/SECURITY.md) - [Changelog](development/docs/CHANGELOG.md)
> - This Repository will auto run RUFF, Black, HTML5Formatter and Dependabot.

## ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `To-Do List` ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png)

- [X] I'm a happy little Placeholder
- [X] I'm a happy little Placeholder
- [ ] I'm a happy little Placeholder
- [ ] I'm a happy little Placeholder

## ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `Security Checklist` ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

`FOR PRODUCTION NEVER FORGET TO DEACTIVATE DEBUG!!!!`
> See [SECURITY.MD](development/docs/SECURITY.md) for deeper explanations.

- [ ] [Jinja2: Enable Autoescaping of all inputs](https://jinja.palletsprojects.com/en/3.1.x/api/)
- [ ] [Flask-WTF: Enable csrf](https://flask-wtf.readthedocs.io/en/0.15.x/csrf/) - [What is CSRF?](https://www.synopsys.com/glossary/what-is-csrf.html)
- [ ] [Care with file uploads!! DIRECTORY TRAVERSAL!](https://flask.palletsprojects.com/en/1.0.x/patterns/fileuploads/)
- [ ] [Activate HTTPS and forbid use of HTTP](https://www.youtube.com/watch?v=Gdys9qPjuKs)
- [ ] [HTTP-Header good practice](https://stackoverflow.com/questions/60566143/what-is-the-best-practice-for-changing-headers-in-a-flask-request) - [HTTP-Headers Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers?retiredLocale=de) - [HTTP-Header list](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
- [ ] Care with syntax for SQL-Injection in SQLAlchemy Models! NEVER use raw SQL! Code line below has SQL-Syntax Highlighting activated and you see the "bad example" glows witl SQL Syntax. !!**That's BAD**!! Never combine the data string with the query string and always use SQLAlchemy [ORM-Model objects](https://docs.sqlalchemy.org/en/20/orm/) to describe a query.
- [ ] Use [Flask-Security](https://pythonhosted.org/Flask-Security/) correctly!
- [ ] [Flask Documentation: Security Considerations](https://flask.palletsprojects.com/en/2.2.x/security/)
- [ ] Only run the Flask app in PRODUCTION behind a reverse proxy like nginx with HTTPS enabled!!!!!!!!!!!!!!!!!
- [ ] [Use OWASP ZAP](https://www.zaproxy.org/) (Penetration Testing) - [OWASP Top10 Vulnerabilities](https://owasp.org/Top10/)