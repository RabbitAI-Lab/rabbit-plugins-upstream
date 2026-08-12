## Description:

Scans e-commerce product titles and listing text for text trademark matches and infringement-risk signals across supported regions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and their agents use this skill to check product titles, bullet points, and descriptions for registered text trademark matches before publishing listings. It helps triage risk but does not provide legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product listing text is sent to LinkFox services and full API responses may be saved locally.

Mitigation: Use the skill only with listing text that is acceptable to share with LinkFox, and review local response and cache files before using it with confidential drafts.

Risk: The bundled onboarding helpers can handle API keys, phone-based login, account lookup, and payment order creation.

Mitigation: Run onboarding, account, or payment helpers only after explicit user intent, and confirm plan and payment details before creating an order.

Risk: Trademark scans consume paid credits, and broad or repeated scans can increase user cost.

Mitigation: Warn users before repeated, broadened, or high-frequency scans, and reuse cached results for the same parameters when appropriate.

## Reference(s):

- [Ruiguan Text Trademark Detection API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ruiguan-text-trademark-detection)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with result tables, shell commands, and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The API response may be printed inline for small results or summarized after writing the full JSON response to a local linkfox session directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
