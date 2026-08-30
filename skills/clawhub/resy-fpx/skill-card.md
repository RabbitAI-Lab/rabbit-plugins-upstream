## Description:

Query and act on Resy restaurant reservations from a shell using curl against api.resy.com, with fpx used only for one-time token bootstrap when Resy credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and advanced agent users use this skill to search Resy venues, inspect availability, book or cancel reservations, and manage favorites or Priority Notify from shell workflows without running the Resy MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to book, cancel, favorite, or delete real Resy reservations and notifications.

Mitigation: Require explicit confirmation of the venue, date, party size, payment method, reservation token, or notify spec before executing any write action, and verify state with list calls before and after changes.

Risk: Resy credentials and auth tokens may be exposed if copied into logs, transcripts, or shared shell history.

Mitigation: Keep RESY_EMAIL, RESY_PASSWORD, and RESY_TOKEN out of logs and transcripts; prefer environment variables or a local secret manager and rotate tokens if exposed.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may perform live Resy account actions when executed with valid credentials or tokens.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
