## Description: <br>
Builds, debugs, and hardens Django applications across models, ORM usage, migrations, views, templates, forms, admin workflows, Django REST Framework APIs, security, performance, testing, upgrades, and deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill for practical Django implementation, debugging, review, hardening, and operational guidance. It helps with framework-specific work such as query optimization, migration planning, authentication, CSRF and deployment issues, DRF APIs, tests, background tasks, and Django upgrades. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can remember Django preferences and project context in ~/Clawic/data/django/. <br>
Mitigation: Install only if that local personalization is acceptable, and review or delete those files when cross-session memory is not desired. <br>
Risk: Django guidance can affect migrations, deployment settings, permissions, CSRF behavior, and production database operations. <br>
Mitigation: Review generated changes before applying them, test against the target settings and database shape, and use backups or staging for risky operational commands. <br>
Risk: HTML examples in Django admin or template code can become unsafe if untrusted data is marked safe. <br>
Mitigation: Use Django's escaping defaults and format_html for generated HTML; avoid mark_safe or safe filters on user-controlled values. <br>


## Reference(s): <br>
- [ClawHub Django Skill](https://clawhub.ai/ivangdavila/skills/django) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Django Skill](https://clawic.com/skills/django) <br>
- [Django Skill Source](artifact/SKILL.md) <br>
- [Django Security Guidance](artifact/security.md) <br>
- [Django Setup and Memory Guidance](artifact/setup.md) <br>
- [Django Memory Template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code, command examples, configuration snippets, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local preference and project-context files under ~/Clawic/data/django/ when present or when the user explicitly provides preferences.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
