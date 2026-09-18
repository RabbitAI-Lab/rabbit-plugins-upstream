## Description:

AgentQL lets an agent operate AgentQL through the OOMOL-connected oo CLI for reading, creating, and updating data without handling raw credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to query webpages with AgentQL, create remote AgentQL browser sessions, and review AgentQL account or session usage through OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to execute remote installer scripts directly, which can run code on the user's machine.

Mitigation: Review the installer path before use, prefer verified or signed official release instructions, and do not allow an agent to run the installer automatically unless the user accepts that execution risk.

Risk: The skill can create remote AgentQL browser sessions and perform other write-tagged actions that change service state.

Mitigation: Confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [AgentQL homepage](https://www.agentql.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL AgentQL connection page](https://console.oomol.com/app-connections?provider=agentql)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AgentQL execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
