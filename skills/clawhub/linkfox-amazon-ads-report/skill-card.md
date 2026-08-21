## Description:

Retrieves Amazon Ads Sponsored Products, Sponsored Brands, and Sponsored Display reports by guiding an agent to select valid report types, columns, grouping, and filters, then create, poll, download, and unpack reports through LinkFox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, agencies, and operators use this skill to retrieve Amazon Ads performance reports for SP, SB, and SD campaigns. Developers and agent users can use it to construct valid report requests, handle long-running report generation, and inspect downloaded report data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon Ads report requests and may process sensitive advertising performance data.

Mitigation: Use the skill only when LinkFox is an acceptable processor for the relevant Amazon Ads data, and treat saved files, terminal logs, local paths, and report URLs as sensitive business data.

Risk: Downloaded reports can be exposed through a temporary localhost HTTP URL by default.

Mitigation: Disable serveExtractedFileHttp for sensitive reports or restrict access to the local machine and retrieve files directly from the saved path.

Risk: The skill can assist account setup and billing recovery when authentication or balance problems occur.

Mitigation: Review account, payment, and billing prompts before acting, and use trusted LinkFox endpoints only.

Risk: Base URL overrides and inline output can expose confidential report data or credentials to untrusted destinations or logs.

Mitigation: Avoid LinkFox API base URL overrides unless the destination is trusted, and avoid --inline for large or confidential data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-report)
- [API and runtime reference](references/api.md)
- [Auth and billing onboarding](references/onboarding.md)
- [Amazon Ads report type catalog](references/report-types/index.md)
- [Amazon Ads API reporting v3 report types](https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries; scripts save full report responses as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full responses are saved under LinkFox session data; large outputs are summarized unless --inline is used; downloaded reports may also be exposed through a temporary localhost URL.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
