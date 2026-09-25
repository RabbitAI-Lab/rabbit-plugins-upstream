## Description:

Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, provides structured data for precision agriculture decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, agricultural producers, and developers use this skill to analyze plant images, videos, or public media URLs and receive plant growth-stage recognition results for precision agriculture decisions. It can also list prior cloud-generated reports associated with the user's resolved account identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media and report data are uploaded to a third-party cloud service for analysis.

Mitigation: Install only if the publisher is trusted and the user is comfortable with cloud media processing.

Risk: The active configuration can use plaintext HTTP even though the skill text describes HTTPS transport.

Mitigation: Require HTTPS-only production endpoints and remove development HTTP configuration before deployment.

Risk: The skill can silently create or reuse a local account identity and store local credentials or tokens.

Mitigation: Review identity creation, local credential storage, and token/database retention before use.

Risk: Report-history lookup can retrieve cloud-stored report metadata.

Mitigation: Narrow history triggers and confirm access controls and retention behavior with the publisher.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [API interface documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown tables and structured JSON or text reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths, public media URLs, history-list requests, and basic, standard, or json detail levels.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
