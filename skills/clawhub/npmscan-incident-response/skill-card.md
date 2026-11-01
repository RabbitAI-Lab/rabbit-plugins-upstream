## Description:

Turns a specific or loosely described npm supply-chain concern into actionable remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[salemalem](https://clawhub.ai/user/salemalem)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and package maintainers use this skill to turn npm supply-chain findings or reported symptoms into remediation plans. It follows findings to relevant response playbooks and explains how to proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remediation advice from the external service may need validation against the package and environment.

Mitigation: Verify the finding and review each suggested step before applying it.

## Reference(s):

- [NPMScan MCP server](https://npmscan.com/api/mcp)
- [ClawHub skill release](https://clawhub.ai/salemalem/skills/npmscan-incident-response)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown with ordered remediation steps and relevant references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to package findings or described symptoms; the skill does not make package changes.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
