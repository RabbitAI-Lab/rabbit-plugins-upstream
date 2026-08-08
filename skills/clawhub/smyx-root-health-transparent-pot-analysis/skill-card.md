## Description:

This skill analyzes images or videos of plant roots in transparent pots, seedling boxes, hydroponic systems, or plant factories to estimate root health, vitality grade, rot indicators, and care-adjustment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit root images or videos for visual plant-root health assessment and to retrieve structured reports or historical report lists. It is intended for care guidance and monitoring, not for definitive agronomic diagnosis or pesticide recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report requests are processed through cloud services.

Mitigation: Use only non-sensitive plant images or videos and run the skill only in environments where external processing is acceptable.

Risk: The skill may silently create or reuse an identity and retrieve identity-linked report history.

Mitigation: Use a dedicated workspace or account for this skill, especially when multiple people share the same environment.

Risk: Account tokens may be stored locally for later API calls.

Mitigation: Review local storage and token handling before installation, and clear stored credentials when the workspace should no longer retain access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-like structured text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a root health score, vitality grade, rot indicators, care guidance, export links, or historical-report tables.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
