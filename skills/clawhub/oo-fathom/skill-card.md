## Description:

Fathom Analytics (usefathom.com) supports reading, creating, and updating Fathom Analytics data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Fathom connector schemas, read account, site, event, milestone, visitor, and aggregation data, and create or update Fathom sites, events, and milestones through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can invoke broad local oo CLI commands, which may affect connected Fathom Analytics resources.

Mitigation: Limit use to Fathom connector schema and run actions, inspect the live schema before building payloads, and confirm create or update payloads before execution.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, pinned, and verifiable method before using the skill.

## Reference(s):

- [Fathom Analytics](https://usefathom.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fathom)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON with data and meta.executionId; write actions require confirmation before execution.]

## Skill Version(s):

1.0.2 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
