## Description:

青虎AI 抖音蓝海爆品采集师 helps an agent combine Douyin trend and keyword video data with 1688 sourcing data to identify blue-ocean product opportunities in niche, high-demand scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Douyin product opportunities, validate niche content demand, compare 1688 supply, estimate margins, and produce a prioritized blue-ocean product shortlist with sourcing and content-angle guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Qinghu API credentials are required and could expose paid data access if reused too broadly.

Mitigation: Keep the Qinghu token scoped to this service, prefer environment variables or direct user input, and avoid echoing credentials in outputs.

Risk: Authorized paid tools may consume Qinghu points, and larger result sets may be exported or reused from local cache files.

Mitigation: Confirm paid-tool authorization, report point consumption when paid tools are used, and share exported files only with the intended user.

Risk: Douyin trend heat, 1688 supply, and margin estimates can be misleading if treated as definitive commercial proof.

Mitigation: Cross-check content demand, supplier availability, pricing assumptions, and sample quality before acting on a product recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-bluesea-collector)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu MCP API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON request examples and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large result sets are expected to be exported to files; paid-tool point usage is summarized when applicable.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
