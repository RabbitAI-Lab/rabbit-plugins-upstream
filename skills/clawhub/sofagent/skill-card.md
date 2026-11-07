## Description:

Provides front-line deployment engineers with a method for enterprise AI deployment, agent governance, change auditing, and continuous improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

External FDEs and enterprise AI teams use this skill to assess business workflows, plan and deliver AI deployments, and maintain them through audits and ongoing improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflows may change persistent agent rules or shared knowledge without clear safeguards.

Mitigation: Begin in an isolated test deployment, review generated skills before activation, test knowledge-base changes on disposable copies, and preserve attributable changes before rollback.

Risk: Business information may be sent to the selected AI provider.

Mitigation: Approve which categories of business information may be shared with the provider.

Risk: The installer and engine are supplied separately from this package and may enable hooks, MCP tools, or scheduled workers.

Mitigation: Review and pin the separately supplied installer and engine before enabling those capabilities.

## Reference(s):

- [Engineering minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Engineering code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [State machine design paper (arXiv:2608.26263)](https://arxiv.org/abs/2608.26263)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Configuration instructions]

**Output Format:** [Markdown plans, assessments, audit reports, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation of enterprise-specific agent skills and knowledge-base entries.]

## Skill Version(s):

1.8.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
