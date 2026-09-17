## Description:

Operates Novu through an OOMOL-connected account for reading, creating, and updating subscribers and triggering workflow events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Novu connector schemas, run Novu actions through the oo CLI, manage subscribers, and trigger workflow events with server-side credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer execution for the oo CLI.

Mitigation: Install the oo CLI from a pinned, verified release or an official package manager before using the skill.

Risk: Novu write actions can create or update subscribers and trigger workflow events.

Mitigation: Check the live action schema, exact JSON payload, and intended effect with the user before allowing write actions.

## Reference(s):

- [Novu Skill Page](https://clawhub.ai/oomol/skills/oo-novu)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Novu Homepage](https://novu.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Novu actions require confirmation of the exact payload and intended effect before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
