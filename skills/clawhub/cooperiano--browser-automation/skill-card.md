## Description:

Browser Automation helps an agent operate web pages, fill forms, take screenshots, extract structured data, manage sessions, upload files, and integrate with the Claude Chrome extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cooperiano](https://clawhub.ai/user/cooperiano)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent drive browser workflows such as navigation, interaction, form submission, screenshots, structured extraction, session reuse, and file upload on sites where they have permission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation may reuse login sessions or cookies and act in authenticated accounts.

Mitigation: Scope tasks to accounts and sites where the user has permission, avoid sharing session artifacts, and request confirmation before sensitive authenticated actions.

Risk: Scraping, proxy use, or anti-bot handling can violate site rules or create abusive traffic patterns.

Mitigation: Respect robots.txt, site terms, and rate limits, and avoid proxy or anti-bot flows unless the user has a legitimate authorized need.

Risk: Form submissions and file uploads can change external systems or disclose user data.

Mitigation: Preview target URLs, fields, files, and intended submissions before execution, and keep uploads limited to approved data.

## Reference(s):

- [ClawHub Browser Automation skill page](https://clawhub.ai/cooperiano/skills/browser-automation)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with browser automation steps, code snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser action plans, selector guidance, screenshot or PDF capture instructions, session-handling guidance, and extraction schemas.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
