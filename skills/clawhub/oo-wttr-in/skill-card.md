## Description:

wttr.in lets an agent retrieve current weather conditions and forecasts from wttr.in through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch current conditions and forecasts from wttr.in as JSON through an OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions direct users to run remote installer scripts for the oo CLI.

Mitigation: Prefer a reviewed, pinned, or package-manager installation path before using the connector.

Risk: Signing into the oo CLI may create persistent local account state.

Mitigation: Authenticate only when a connector command fails for authentication, and use an account appropriate for the environment.

Risk: Weather requests are routed through OOMOL's oo CLI and connector.

Mitigation: Install and use this skill only when that routing path is acceptable for the task and environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wttr-in)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [wttr.in homepage](https://wttr.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The get_weather action is read-only; first-time use may require oo CLI installation and OOMOL authentication.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
