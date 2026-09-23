## Description:

Recognizes cat and dog vocalizations and returns AI-inferred emotions and behavioral intentions, with structured reports, report links, and history lookup for prior analyses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet audio or video for cloud-based cat and dog vocal emotion analysis, then receive a structured result and a report link. The skill can also retrieve prior pet vocal emotion analysis reports associated with the current local/cloud identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media and report queries are sent to a cloud service.

Mitigation: Review the skill before installing and use it only with media approved for that cloud service.

Risk: Activity is automatically linked to a local/cloud identity and reusable tokens may be stored in a workspace database.

Mitigation: Run in an isolated workspace, review token storage behavior, and clear generated identity or token data after use where required.

Risk: The packaged configuration includes development HTTP endpoints and a broad common API layer flagged by the security guidance.

Mitigation: Fix or justify development endpoints before use with private media or real accounts, and restrict allowed network targets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Vocal Emotion Analysis API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Structured text or JSON with Markdown report links and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exported report image links and paginated history report data.]

## Skill Version(s):

1.0.13 (source: server evidence release; artifact frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
