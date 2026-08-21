## Description:

Checks product images against Ruiguan's design patent database to surface similar patents, TRO history, and radar-based infringement indicators across 25+ regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, IP professionals, and developers use this skill to submit product images and context to LinkFox Ruiguan for design patent similarity search, TRO history checks, and risk-oriented result summaries before listing products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, product descriptions, account credentials, and billing actions may be sent through LinkFox services.

Mitigation: Use this skill only when sharing those materials with LinkFox is acceptable, and avoid confidential product designs unless public upload and third-party processing are approved.

Risk: Patent detection calls consume LinkFox credits and may trigger billing or account onboarding flows.

Mitigation: Confirm expected credit use with the user before running paid searches, prefer cached results for repeated parameter sets, and manage payments deliberately.

Risk: Local product images are uploaded to obtain public URLs, and full API responses are persisted locally.

Mitigation: Review and remove generated public image links and saved result files when they are no longer needed, especially in shared workspaces.

Risk: The detection result is not legal advice and may be incomplete or misleading if treated as a final infringement determination.

Mitigation: Present results faithfully, highlight similarity and TRO indicators, and direct users to consult a qualified IP attorney for legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-detection-patent-design)
- [睿观-外观专利检测 API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, stdout summaries, and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a public image URL and a LinkFox API key; API responses are cached for 24 hours and full results are saved under a LinkFox session data directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
