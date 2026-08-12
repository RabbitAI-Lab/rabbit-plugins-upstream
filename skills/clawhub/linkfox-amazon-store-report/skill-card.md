## Description:

Automates Amazon seller report retrieval for inventory, orders, sales traffic, FBA, financial settlement, returns, and Brand Analytics reports, including request, polling, download, extraction, and local preview links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to pull structured Amazon Seller reports for authorized stores after selecting a seller account through the companion LinkFox authorization skill. It is intended for report acquisition and file delivery, not business interpretation of the downloaded data.

### Deployment Geography for Use:

Global, limited to the Amazon SP-API regions and marketplaces supported by the skill.

## Known Risks and Mitigations:

Risk: Amazon seller reports and API credentials can contain sensitive business data.

Mitigation: Treat downloaded reports and returned API keys as sensitive, avoid exposing Amazon source URLs unless needed for troubleshooting, and keep report outputs local.

Risk: Downloaded report files may be briefly served over local HTTP.

Mitigation: Keep the HTTP bind host on 127.0.0.1, avoid broad or public interfaces, and use a short serving window.

Risk: Account, billing, and payment setup guidance can trigger user decisions outside normal report retrieval.

Mitigation: Review any account or purchase step before approving it, and stop for user confirmation when authentication or billing errors require action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-report)
- [Amazon store report API reference](references/api.md)
- [Report type values](references/report-types.md)
- [Report request schemas](references/report-requests/README.md)
- [Script usage guide](scripts/README.md)
- [Amazon SP-API report type values](https://developer-docs.amazon.com/sp-api/docs/report-type-values)
- [Amazon Selling Partner API report schemas](https://github.com/amzn/selling-partner-api-models/tree/main/schemas/reports)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Files, Configuration guidance]

**Output Format:** [Markdown guidance, shell commands, and JSON results containing report identifiers, local file paths, file URIs, and short-lived local HTTP download URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes downloaded and extracted report files locally; may briefly serve the extracted file over 127.0.0.1 for browser download.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
