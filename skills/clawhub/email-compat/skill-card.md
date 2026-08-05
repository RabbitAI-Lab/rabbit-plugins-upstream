## Description:

Write and verify HTML email that renders correctly across email clients using caniemail.com compatibility data and authoring rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, edit, and review HTML email templates and transactional messages for rendering compatibility across clients such as Outlook, Gmail, and Apple Mail. It supports compatibility lookup, markup linting, and client-specific workaround guidance, but it does not cover sending mail, deliverability, authentication, list management, or ESP selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Normal use may request public compatibility data from caniemail.com and store a local cache.

Mitigation: Use the documented offline flag when network refreshes are not desired, and rely on the bundled dataset snapshot with the reported data source warning.

Risk: Email client compatibility data can be stale or untested for some features.

Mitigation: Check the reported verdict, notes, last test date, staleness, and data source before treating a feature as safe for production email.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shbernal/skills/email-compat)
- [caniemail.com](https://www.caniemail.com)
- [caniemail data API](https://www.caniemail.com/api/data.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results distinguish supported, unsupported, mitigated, and untested verdicts and include data source freshness when available.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
