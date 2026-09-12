## Description:

Evaluates Xinchuan and IT information-technology bid opportunities by using bid-history data to assess whether to bid, likely competitors, buyer patterns, pricing benchmarks, technical-fit risks, and reportable next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to evaluate a specific IT, Xinchuan, software, systems-integration, cloud, data-center, cybersecurity, or smart-city procurement opportunity. It produces a decision report covering bid/no-bid posture, buyer behavior, incumbent supplier signals, competitor forecast, comparable pricing, risk factors, and recommended actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid-search terms are sent to the vendor service during analysis.

Mitigation: Use the skill only for projects whose search terms can be shared with the vendor, and avoid submitting sensitive local file contents unless required by the workflow.

Risk: Optional auto-registration sends platform, CPU architecture, and a MAC-derived device hash for trial-account deduplication.

Mitigation: Set your own ZLBX_API_KEY before use to skip auto-registration, or proceed only after confirming that this device fingerprinting is acceptable.

Risk: API keys are stored in ~/.zlbx/config.json when automatic registration succeeds.

Mitigation: Review file permissions on ~/.zlbx/config.json and avoid sharing logs, screenshots, or reports that expose credentials or signed links.

Risk: Generated HTML reports may persist bid details, signed sk links, and analysis conclusions on disk.

Mitigation: Review the HTML report before sharing and remove signed links or sensitive commercial conclusions when distribution is not intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/xinchuang-it-bid-decision)
- [Workflow guide](artifact/references/workflow.md)
- [API quick reference](artifact/references/api-quick.md)
- [Report template](artifact/references/report-template.md)
- [Auto-registration workflow](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account and registration portal](https://ai.zhiliaobiaoxun.com/?ch=s82)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown decision report in chat, with an optional self-contained HTML report file generated from structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include data-source notes, confidence, data gaps, cited bid/company records when available, and a disclaimer.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
