## Description:

Helps agents read Linear issues, comments, and account details through an OOMOL-connected Linear MCP account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Linear can ask an agent to retrieve issues, issue comments, and their account details without handling raw access tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup offers a remote install script that has not been verified.

Mitigation: Prefer a trusted package manager or verified CLI release; review the installer before running a downloaded script.

Risk: Linear data passes through OOMOL's connector service.

Mitigation: Confirm that sharing the relevant Linear data with OOMOL meets your organization's requirements.

## Reference(s):

- [Linear MCP documentation](https://linear.app/docs/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Linear MCP skill on ClawHub](https://clawhub.ai/oomol/skills/oo-linear-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Linear issue, comment, and user information.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
