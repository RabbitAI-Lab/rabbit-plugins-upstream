## Description:

Use Workiz through an OOMOL-connected account to search and read jobs, leads, and active team members with the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to retrieve Workiz jobs, leads, and active team member records from an OOMOL-connected Workiz account. Agents use it when they need guided read-only Workiz access without handling raw Workiz tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that setup instructions execute remote installer scripts.

Mitigation: Review the OOMOL CLI installation path before installing, and prefer a pinned package-manager or verified release method.

Risk: The skill can read Workiz account data through the connected OOMOL connector.

Mitigation: Connect only a Workiz account whose jobs, leads, and team member records are appropriate for the agent to read.

## Reference(s):

- [ClawHub Workiz Skill Page](https://clawhub.ai/oomol/skills/oo-workiz)
- [Workiz Homepage](https://www.workiz.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
