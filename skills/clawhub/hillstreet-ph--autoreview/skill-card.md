## Description:

Structured code review when explicitly requested, preferring OpenAI/Codex before Claude.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use Auto Review to request independent reviews of local changes, branches, or commits, with controls for review scope, context, and severity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review findings are advisory, and the supplied scan evidence is incomplete.

Mitigation: Verify findings against the reviewed changes and supplied evidence; consider whether the documented model and API choices suit your account and expectations.

## Reference(s):

- [Diagnostics and result guidance](references/diagnostics-and-results.md)
- [GPT-6.1 Sol model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
- [GPT-6 Sol model documentation](https://developers.openai.com/api/docs/models/gpt-6-sol)
- [GPT-6 Luna model documentation](https://developers.openai.com/api/docs/models/gpt-6-luna)
- [Codex reasoning modes](https://learn.chatgpt.com/docs/models#know-when-to-use-max-or-ultra)
- [AutoReview on ClawHub](https://clawhub.ai/hillstreet-ph/skills/autoreview)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown review report with optional validated JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports review findings, status, and observed usage when available. Findings are advice to verify, not instructions to apply blindly.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
