## Description:

Analyzes Xiaohongshu accounts using recent account data to produce seven-dimension diagnostic reports, similar-account recommendations, multi-account comparisons, and HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External Xiaohongshu creators, MCN and content operations teams, and brands use this skill to diagnose account health, benchmark recent performance, compare multiple accounts, and identify actionable optimization steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and sends Xiaohongshu account IDs to RedFox and search providers.

Mitigation: Use a revocable API key, confirm its scope and expiry, and analyze only accounts you are authorized to assess.

Risk: Generated output files may retain Xiaohongshu account data.

Mitigation: Treat generated reports and JSON files as account data, limit sharing, and delete retained outputs when they are no longer needed.

Risk: The security assessment notes a TLS verification bypass and remote CDN scripts.

Mitigation: Fix these issues or explicitly accept them before normal use.

Risk: The 30-minute subscription flow can trigger delayed sync and report behavior.

Mitigation: Review the subscription flow and user consent before enabling delayed report delivery.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-account-analyzer)
- [API interface and scoring logic](references/api_guide.md)
- [Xiaohongshu account analysis workflow guide](references/workflow_guide.md)
- [Diagnostic report template](references/report_template.md)
- [Benchmark data reference](references/benchmark_data.md)

## Skill Output:

**Output Type(s):** [text, markdown, HTML, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnostic reports, JSON report data, HTML report files, and shell commands for querying and rendering reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a REDFOX_API_KEY; sends Xiaohongshu account IDs to RedFox and may retain generated account data in output files.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
