## Description:

Query and act on Resy restaurant reservations from a shell using curl against api.resy.com, with optional one-time fpx token bootstrap when Resy email/password credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to search Resy venues, inspect availability, book or cancel reservations, and manage favorites or Priority Notify from shell workflows. It is intended for agents preparing or running Resy account commands with explicit user oversight for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare or run commands that book, cancel, favorite, or create notification requests on a real Resy account.

Mitigation: Require explicit user confirmation before running any mutating command and verify account state with list or profile calls before and after write actions.

Risk: Resy tokens, account credentials, browser-session access, and returned profile or payment metadata are sensitive.

Mitigation: Keep tokens and credentials out of logs and shared transcripts, use environment variables for secrets, and avoid exposing profile or payment metadata unless needed for the task.

## Reference(s):

- [Resy API reference](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that access account profile, payment metadata, reservations, favorites, and notification settings when run with valid Resy credentials or token.]

## Skill Version(s):

0.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
