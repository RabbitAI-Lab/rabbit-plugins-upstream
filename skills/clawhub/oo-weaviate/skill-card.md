## Description:

Enables agents to inspect Weaviate action schemas and read collections, objects, and instance metadata through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent query Weaviate collection definitions, objects, instance metadata, and live connector schemas through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can direct an agent toward executing an unverified remote installer for the oo CLI.

Mitigation: Require a human to review the installer source, prefer a signed or packaged install path when available, and approve CLI installation or login steps before execution.

Risk: The skill depends on OOMOL as the connector and credential broker for the user's Weaviate account.

Mitigation: Install only when the user accepts OOMOL-mediated access, and use the OOMOL connection page to manage or revoke Weaviate credentials.

## Reference(s):

- [Weaviate homepage](https://weaviate.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-weaviate)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution and returns connector data with execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
