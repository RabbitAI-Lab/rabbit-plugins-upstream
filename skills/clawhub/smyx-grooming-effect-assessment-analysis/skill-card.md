## Description:

Assesses post-grooming pet images or videos for mat residue, dandruff coverage, and coat smoothness, then returns a grooming score and follow-up care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, grooming-service operators, and agent operators use this skill to evaluate grooming quality from pet photos or videos, including mat residue, dandruff coverage, coat smoothness, and whether follow-up grooming or care is suggested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos may be sent to the LifeEmergence cloud service for analysis.

Mitigation: Use the skill only when cloud processing of the submitted media is acceptable, and avoid sensitive media unless the service terms and data handling are approved.

Risk: The skill can silently create or reuse a persistent local identity and token database in the workspace.

Mitigation: Run it in a controlled workspace and review publisher guidance for inspecting, rotating, or deleting stored identity and token data.

Risk: The skill can query identity-linked historical reports without clear user control.

Mitigation: Review history lookup behavior before deployment and limit use to contexts where identity-linked report retrieval is expected.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON analysis report with score, observations, suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can analyze local files or URLs and can list identity-linked historical reports through the configured cloud service.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
