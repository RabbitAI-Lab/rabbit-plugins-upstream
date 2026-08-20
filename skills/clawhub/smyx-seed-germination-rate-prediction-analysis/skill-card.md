## Description:

Analyzes seedling tray images or videos to identify emerged seedlings, count germinated seeds, estimate germination rate, and return structured analysis or history reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, greenhouse operators, seed testing teams, and developers use this skill to analyze seedling tray media, estimate germination rates, and retrieve cloud-stored report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Seed tray images, videos, and report-history requests are sent to a vendor cloud service.

Mitigation: Use only media that is acceptable to share with the vendor service, and confirm retention, deletion, and access policies before using sensitive agricultural, business, or location-revealing content.

Risk: The skill creates or reuses an internal identity and stores authentication tokens locally for account-linked report access.

Mitigation: Run in an isolated agent workspace, review local credential storage expectations, and clear stored identity or token data when the skill is no longer needed.

Risk: The scanner verdict is suspicious because account-linked cloud access happens quietly.

Mitigation: Review the publisher and service terms before installation, and restrict use to environments where this account-linking behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with structured JSON content, report links, and optional file output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can query historical reports from the vendor cloud service and can write results to a local output file when requested.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
