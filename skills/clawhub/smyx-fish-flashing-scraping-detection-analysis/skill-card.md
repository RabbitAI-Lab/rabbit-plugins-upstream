## Description:

Analyzes aquarium media for fish flashing and scraping, reporting behavior-based ectoparasite risk warnings and suggested follow-up observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquaculture operators use this skill to review fish rubbing behavior in camera footage, receive possible ectoparasite warnings, and consult historical reports. Warnings are not a diagnosis and should be followed by direct observation and veterinary assessment when warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media or media URLs are sent to external cloud services.

Mitigation: Share media only when acceptable under your privacy and data-handling requirements.

Risk: The skill can create or reuse local account state and persist identity tokens while retrieving report history.

Mitigation: Review or clear the workspace data database if persistent identity tokens are unacceptable, and check cloud history access before use.

Risk: Behavior-based warnings may be mistaken for a definitive parasite diagnosis.

Mitigation: Treat alerts as preliminary; inspect fish and seek veterinary microscopy for diagnosis and treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis reports and Markdown history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event counts, risk levels, recommended actions, and report links.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
