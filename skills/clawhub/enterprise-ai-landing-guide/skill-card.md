## Description:

Helps businesses answer up to six dynamic questions to identify a 7-day AI validation scenario and, with separate consent, request Blueprint FDE human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yliu35126-afk](https://clawhub.ai/user/yliu35126-afk)

### License/Terms of Use:

MIT-0

## Use Case:

Business teams, operators, and consultants use this skill to turn a known business problem or lightweight opportunity scan into a prioritized AI landing map. The map separates confirmed facts, file evidence, AI inferences, and open questions while outlining human responsibilities, a 7-day validation plan, 30-day metrics, stop conditions, and optional FDE human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided business information or attachments are sent to a disclosed remote service.

Mitigation: Confirm the API base URL is the official HTTPS service, upload only data the user is authorized to share, avoid secrets or highly sensitive personal data, and review the privacy notice before use.

Risk: Generated business guidance could mix confirmed facts with AI inferences or unsupported numeric targets.

Mitigation: Keep confirmed facts, file evidence, AI inferences, and open questions separate, and mark unsupported costs, benefits, losses, percentages, or targets as pending confirmation.

Risk: Optional FDE human review can store the generated map and company information after consent.

Mitigation: Use separate consent for storage and contact, and request conversion only after storage consent and a user-provided company name are present.

Risk: Session tokens or service credentials could be exposed if copied into logs, files, screenshots, or summaries.

Mitigation: Keep session tokens only in the current process environment and do not write tokens, API keys, cookies, database details, or real customer contact data into the skill package or logs.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/yliu35126-afk/skills/enterprise-ai-landing-guide)
- [Product homepage](https://fde.lantuzhigou.com/enterprise-ai-landing-guide)
- [Public OpenAPI](https://fde.lantuzhigou.com/api/public/clawhive/v1/openapi.yaml)
- [API calling contract](references/API.md)
- [Output explanation](references/OUTPUT.md)
- [Usage boundaries](references/usage-boundaries.md)
- [Privacy notice](https://fde.lantuzhigou.com/legal/clawhive/privacy)

## Skill Output:

**Output Type(s):** [guidance, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown narrative with a structured JSON landing map and optional shell commands for API checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ENTERPRISE_AI_LANDING_API_BASE and uses separate consent gates before FDE human review.]

## Skill Version(s):

1.2.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
