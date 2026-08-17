## Description:

Machine Purchase ROI Gate helps an agent decide whether to buy one machine service call before payment by validating price, fee, failure, retry, value, and budget assumptions, calculating expected return measures, and returning buy, defer, or reject with the binding reason.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentpmt](https://clawhub.ai/user/agentpmt)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to gate a bounded AgentPMT machine-service purchase before any payment is authorized. It is intended to make the economic assumptions explicit, validate them, compute expected net value and ROI, and report a compact machine-readable decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A caller could trust the workflow without reviewing the linked AgentPMT setup and tool skills it depends on.

Mitigation: Confirm trust in AgentPMT, the account setup workflow, and the linked validation and mathematics skills before installing or using the workflow.

Risk: Incorrect or incomplete purchase assumptions could produce an unreliable ROI decision.

Mitigation: Use the workflow's validation step to reject malformed JSON, missing values, non-finite numbers, invalid probabilities, negative money values, zero outlay, or recovery greater than outlay before calculating return.

Risk: A financial decision could be mistaken for payment authorization.

Mitigation: Keep the workflow limited to pre-payment analysis; the inspected skill explicitly says not to access a wallet, sign, pay, or broadcast.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/machine-purchase-roi-gate)
- [AgentPMT Workflow Page](https://www.agentpmt.com/agent-workflow-skills/machine-purchase-roi-gate)
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt)
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup)
- [Data Format Validation](https://clawhub.ai/agentpmt/data-format-validation)
- [Complex Mathematics Engine](https://clawhub.ai/agentpmt/complex-mathematics-engine)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, API Calls, Configuration instructions]

**Output Format:** [Markdown and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a compact machine-readable buy, defer, or reject decision with the binding reason; it explicitly does not access a wallet, sign, pay, or broadcast.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
