## Description:

Massive (Polygon.io) provides OOMOL-connected access to Polygon.io market, reference, options, indicator, macroeconomic, news, and calendar data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Polygon.io connector schemas and run read-oriented market data actions through an OOMOL-connected account without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes one-line remote installer commands that could modify the local environment if run automatically or without review.

Mitigation: Review and install the oo CLI through a trusted, documented path; do not allow an agent to run the remote installer automatically unless the installer source and sign-in implications are accepted.

## Reference(s):

- [Massive (Polygon.io) homepage](https://massive.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-polygon-io)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions are run with JSON payloads after inspecting the live action schema.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
