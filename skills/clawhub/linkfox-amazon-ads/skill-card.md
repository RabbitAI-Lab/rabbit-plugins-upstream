## Description:

LinkFox Amazon Ads is a one-stop Amazon Ads toolkit for LWA authorization and token management, SP/SB/SD campaign entity querying and create/update operations, and end-to-end advertising report retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, advertisers, and operators use this skill to authorize Amazon Ads accounts, inspect or update SP/SB/SD campaign structures, adjust bids, budgets, and statuses after confirmation, and retrieve structured performance reports.

### Deployment Geography for Use:

Global, subject to Amazon Ads marketplace availability and LinkFox service availability.

## Known Risks and Mitigations:

Risk: The skill handles LinkFox and Amazon Ads authorization flows and ad-account credentials.

Mitigation: Install only in trusted workspaces, avoid shared environments, and treat generated LinkFox data files and report temp files as sensitive.

Risk: The skill can create or update ads, bids, budgets, and statuses.

Mitigation: Require a clear confirmation summary before write operations and review the returned operation receipt after execution.

Risk: Full outputs are persisted locally and reports can be served through a temporary local HTTP link.

Mitigation: Restrict access to the workspace, remove sensitive output files when no longer needed, and disable report HTTP serving when a browser download link is unnecessary.

Risk: Secret-bearing requests can be sent to configurable gateway URLs.

Mitigation: Keep gateway-related environment variables pointed only at trusted LinkFox HTTPS hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads)
- [Amazon Ads Authorization Reference](references/linkfox-amazon-ads-auth.md)
- [Amazon Ads Management Reference](references/linkfox-amazon-ads-manager.md)
- [Amazon Ads Reporting Reference](references/linkfox-amazon-ads-report.md)
- [Sponsored Products API Reference](references/api/sp.md)
- [Sponsored Brands API Reference](references/api/sb.md)
- [Sponsored Display API Reference](references/api/sd.md)
- [Report Type Reference Index](references/report-types/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown summaries with JSON responses, local JSON files, authorization URLs, report links, and shell command invocations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are persisted locally under linkfox session data; tokens are masked in normal output; report retrieval can expose a temporary local HTTP link.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
