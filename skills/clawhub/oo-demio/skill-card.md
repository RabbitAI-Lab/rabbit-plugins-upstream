## Description:

Operates Demio through the OOMOL-connected oo CLI to read event data, inspect sessions and participants, and register attendees without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a connected Demio account for webinar and event lookup, session and participant retrieval, and attendee registration. It is suited to Demio workflows where reads can run directly and write actions require confirmation of the exact payload and effect.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI only from a trusted, versioned, verified source.

Risk: The skill can register Demio attendees and change account state through actions tagged as writes.

Mitigation: Confirm the exact payload and expected effect with the user before running write or destructive actions.

Risk: The connector acts through the Demio account and scopes connected in OOMOL.

Mitigation: Connect only the intended Demio account and scopes, and reconnect deliberately when credentials expire or scopes are missing.

## Reference(s):

- [ClawHub Demio skill page](https://clawhub.ai/oomol/skills/oo-demio)
- [Demio homepage](https://www.demio.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
