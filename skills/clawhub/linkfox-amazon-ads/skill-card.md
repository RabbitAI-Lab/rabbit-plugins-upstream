## Description:

LinkFox Amazon Ads helps agents authorize Amazon Ads accounts, manage SP/SB/SD campaign entities, and retrieve structured advertising reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External advertisers, agencies, and e-commerce operators use this skill to connect Amazon Ads accounts, inspect or update SP/SB/SD campaign entities, and pull structured performance reports. It is intended for workflows where an agent needs authenticated Amazon Ads access, campaign management actions, or report retrieval with user review around spend-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Amazon Ads accounts and make changes that affect advertising spend.

Mitigation: Install only when the publisher is trusted, require clear user confirmation before spend-changing create or update actions, and review returned operation receipts.

Risk: API keys, OAuth tokens, generated JSON files, report temp files, and logs may contain sensitive account or advertising data.

Mitigation: Treat generated files and logs as sensitive, avoid exposing token values, and clean up local outputs when they are no longer needed.

Risk: Changing gateway or login URL environment variables can redirect credentials or advertising data to untrusted endpoints.

Mitigation: Set URL override environment variables only for endpoints you control and audit.

Risk: Extracted report files may be temporarily exposed through a local HTTP link.

Mitigation: Disable report HTTP serving when not needed, keep links private, and rely on the local file path for sensitive reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads)
- [Amazon Ads authorization reference](references/linkfox-amazon-ads-auth.md)
- [Amazon Ads management reference](references/linkfox-amazon-ads-manager.md)
- [Amazon Ads reporting reference](references/linkfox-amazon-ads-report.md)
- [SP/SB/SD API references](references/api/)
- [Report type specifications](references/report-types/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON parameters, shell commands, local JSON file paths, and structured Amazon Ads results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may write complete responses and reports to local JSON files while printing summaries for large outputs; tokens are expected to be masked in user-facing output.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
