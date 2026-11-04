## Description:

Analyzes close-up pet eye images or videos for visible redness, tearing, and cloudiness, then returns alerts and structured reports to support early veterinary follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary teams can use the skill to review close-up images or videos for visible eye changes and retrieve prior reports. Its findings are visual prompts and do not replace a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account handling may mix users and associate report history with the wrong person.

Mitigation: Avoid shared-workspace use until sender isolation is corrected; use a separate trusted account for each user.

Risk: The export-only option may still upload selected footage, and analysis sends media to LifeEmergence.

Mitigation: Do not use export-only with sensitive footage; obtain consent before uploading and use the service only when its data handling is acceptable.

Risk: The skill may create an account, incur charges, and store a token locally; provider retention and server-side access controls are unverified.

Mitigation: Review account and billing implications first, protect local token storage, and avoid uploading footage until provider retention and access controls are understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-eye-anomaly-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured analysis reports and alerts, with Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes visual findings, risk prompts, recommendations, and report links; not a veterinary diagnosis.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
