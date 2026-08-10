## Description:

Helps enterprises identify one AI-first opportunity that can be validated within 7 days using up to six dynamic questions, then request Blueprint FDE human review after separate user consents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yliu35126-afk](https://clawhub.ai/user/yliu35126-afk)

### License/Terms of Use:

MIT-0

## Use Case:

Business users use this skill to turn a known problem or lightweight opportunity scan into an AI landing map with a first-priority scenario, human responsibilities, a 7-day validation path, 30-day metrics, stop conditions, and optional FDE human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business process details and selected attachments are sent to an external HTTPS service.

Mitigation: Use only information the user is authorized to share, exclude trade secrets and regulated personal data, and review the disclosed service destination before installation.

Risk: FDE human review or contact sharing could expose company and contact information beyond the anonymous session.

Mitigation: Require separate consent for storage/review and for contact sharing; do not send contact details unless the user explicitly opts in.

Risk: The generated landing map may include AI inferences or suggested targets that are not verified business facts.

Mitigation: Display confirmed facts, file evidence, AI inferences, and pending confirmations separately, and mark unsupported numeric targets as suggestions that need confirmation.

## Reference(s):

- [API Calling Contract](references/API.md)
- [Output Guide](references/OUTPUT.md)
- [Usage Boundaries](references/usage-boundaries.md)
- [Public OpenAPI Specification](https://101.37.87.144/api/public/clawhive/v1/openapi.yaml)
- [ClawHub Skill Page](https://clawhub.ai/yliu35126-afk/skills/enterprise-ai-landing-guide)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, API Calls, Shell Commands, Configuration]

**Output Format:** [Structured JSON and Markdown, with optional shell commands for the bundled API client]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates confirmed facts, file evidence, AI inferences, and items that need confirmation; does not guarantee business outcomes.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
