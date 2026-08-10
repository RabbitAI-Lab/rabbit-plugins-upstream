## Description:

Analyzes cat litter-box images, videos, local files, or URLs with a cloud service to produce structured observations about feces morphology, urine clump size, and health risk alerts without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat litter-box media for standardized waste-characteristic observations, monitoring trends, and report links. It is intended for smart litter boxes and multi-cat household health monitoring, with outputs framed as health references rather than diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Litter-box media or URLs are sent to the configured cloud service for analysis.

Mitigation: Use the skill only when cloud processing of the media is acceptable and review the service's retention and deletion practices before sharing sensitive content.

Risk: The skill can silently create or reuse a persistent local or backend identity and tokens.

Mitigation: Review token storage and identity behavior before installation, and prefer a release that asks before account creation or clearly documents token lifecycle controls.

Risk: History lookup can retrieve cloud-hosted reports associated with the resolved identity.

Mitigation: Run history lookup only when report retrieval is expected, and verify that users understand which account or identity is being queried.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-litter-box-waste-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text reports, with optional JSON-oriented detail and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured observations, health risk alerts, recommendations, history tables, and report links.]

## Skill Version(s):

1.0.6 (source: server release metadata; SKILL.md frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
