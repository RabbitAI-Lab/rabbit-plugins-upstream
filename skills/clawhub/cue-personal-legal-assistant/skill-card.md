## Description:

Provides personalized legal research and guidance, comparisons with similar cases, damages estimates, and drafts or reviews legal documents with source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and lawyers use the skill to research legal questions, compare similar cases, review laws, estimate claims, and draft or review legal documents. Its outputs support research and preparation; important decisions and legal documents should receive qualified human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to paste an API key into chat.

Mitigation: Use protected credential configuration instead of chat, and rotate any key already shared.

Risk: The skill automatically installs or updates an external runner whose behavior has not been verified.

Mitigation: Use a reviewed, pinned runner version and retain explicit control over installation and updates.

Risk: Legal case details and reports may contain sensitive information, and retention or report-sharing protections need confirmation.

Mitigation: Redact sensitive case details and check Cue's retention and report-sharing protections before use.

Risk: Research runs may consume paid credits.

Mitigation: Confirm paid runs before starting them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-personal-legal-assistant)
- [Cue legal playbook](https://cuecue.cn/playbook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown reports and legal document drafts with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research outputs and drafts require human review; they are not formal legal opinions or a substitute for legal representation.]

## Skill Version(s):

1.3.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
