## Description:

Analyzes plant images, videos, optional environmental data, and growth metrics to produce a 0-100 plant vitality score, vitality grade, trend, change percentage, and alert hint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate plant vitality from plant media, optional environmental readings, and growth indicators. It supports smart planters, home gardening, plant factories, and plant-monitoring platforms that need structured vitality reports and history lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and account-linked metadata may be sent to configured remote services for analysis.

Mitigation: Review the configured service endpoints and obtain user consent before installing or running the skill with plant images, videos, URLs, or environment data.

Risk: History requests automatically fetch cloud report records associated with the resolved identity.

Mitigation: Use history lookup only when the user requests it, and disclose that results come from the remote service account context.

Risk: The skill creates or reuses a local identity and can persist authentication tokens locally.

Mitigation: Make authentication and persistence opt-in or clearly consented, and clear local credentials when the skill is no longer needed.

Risk: Default configuration includes remote service endpoints and automatic network calls.

Mitigation: Review endpoint configuration before deployment and remove development or private endpoints from release defaults.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [Plant Vitality API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports, with optional report links and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an analysis result to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
