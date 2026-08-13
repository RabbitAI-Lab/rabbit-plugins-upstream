## Description:

Builds, updates, runs, and validates a SmartLink / Zhijietong cross-border ecommerce intellectual-property HTML workbench for patent workflows, compliance checks, infringement response, knowledge search, local preview, and PatSnap/Zhihuiya-backed data access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to maintain a local, customer-facing SmartLink intellectual-property workbench for cross-border ecommerce workflows including infringement complaints, listing compliance, competitor patent analysis, and knowledge support. It also guides local service startup, HTML validation, backup/latest-file handling, and PatSnap/Zhihuiya MCP setup checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill edits a specific local HTML file and creates backup/latest copies under hard-coded Downloads paths.

Mitigation: Use it only in the intended SmartLink/PatSnap workstation context and confirm target paths before allowing file edits or backup operations.

Risk: The skill may start or rely on localhost services on ports 8767 and 8788.

Mitigation: Check that the local HTTP and proxy services are expected for the task, bound to localhost, and not conflicting with other services.

Risk: PatSnap/Zhihuiya MCP credentials and services must be configured separately for live data workflows.

Mitigation: Run the documented MCP connectivity check before relying on live patent data, and treat results as analysis framework output if MCP access is unavailable.

## Reference(s):

- [Competitor Analysis Implementation Notes](references/competitor-analysis.md)
- [PatSnap Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [PatSnap MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/smartlink-ip-workbench)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown with inline file paths, URLs, shell commands, and code-oriented implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local HTML files, backup copies, latest-file copies, validation output, and localhost service instructions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
