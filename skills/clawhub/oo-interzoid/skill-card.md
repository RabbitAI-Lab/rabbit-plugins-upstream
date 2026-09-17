## Description:

Provides OOMOL-connected access to Interzoid actions for searching, reading, validating, enriching, and standardizing Interzoid data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Interzoid connector actions through an OOMOL-connected account, including match-key generation, email enrichment, IP profile lookup, credit checks, and organization-name standardization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include running remote installer scripts directly in a shell.

Mitigation: Review setup steps before installation, prefer a trusted versioned oo CLI package or verified installer, and do not let an agent run the remote installer automatically.

Risk: Connector actions depend on an authenticated OOMOL account and connected Interzoid credentials.

Mitigation: Run setup or reconnection steps only after an auth or connection error, and avoid exposing raw API tokens to the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-interzoid)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Interzoid homepage](https://www.interzoid.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector output is returned as JSON data with execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
