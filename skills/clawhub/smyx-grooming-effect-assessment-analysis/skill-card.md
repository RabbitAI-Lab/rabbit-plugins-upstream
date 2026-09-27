## Description:

Assesses post-grooming pet images or videos for remaining mats, dandruff, and coat smoothness, then provides a grooming score and follow-up suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming professionals use the skill to review post-grooming photos or videos, assess grooming quality, and decide whether additional brushing or care may be needed. It can also retrieve past assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, or supplied URLs are sent to a configured cloud service for analysis.

Mitigation: Submit only media and URLs you have permission to share, and avoid private household imagery unless you trust the provider.

Risk: The skill creates or reuses a local identity, stores tokens, and links cloud report history to that identity with limited user control.

Mitigation: Review the workspace data directory for saved identity or token databases when removing the skill, and avoid history queries if you do not want cloud records accessed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON assessment; Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a 0–100 grooming score, care suggestions, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
