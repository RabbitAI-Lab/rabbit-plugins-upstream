## Description:

Audits MCP host configuration by collecting server entries, flagging common exposure patterns, and producing a risk-ranked review with hardening guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review MCP server configurations before adoption or to understand what capabilities existing host configurations grant. It produces prioritized configuration hardening guidance while keeping server implementation and runtime behavior outside the review scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local MCP configuration, which can expose server commands, endpoints, and credential-related variable names to the audit report.

Mitigation: Run it only when you intend to review those configurations; its collector reports environment and header key names and whether values exist, not the values themselves.

Risk: The security evidence reports an unresolved local reference and says scan evidence is incomplete.

Mitigation: Review the complete release contents and resolve the local reference before relying on the scan assessment.

## Reference(s):

- [Skill source repository](https://github.com/z-Zihan/awesome-skills)
- [MCPHallu paper](https://arxiv.org/abs/2611.07689)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Configuration instructions, Guidance]

**Output Format:** [Markdown report with tables, risk tiers, and prioritized hardening recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configuration-focused findings; environment and header values are redacted, and MCP servers are not executed.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
