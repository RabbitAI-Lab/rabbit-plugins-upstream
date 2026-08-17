## Description:

Recognizes cat and dog barks through pet voiceprint AI and returns emotions and behavioral intentions such as happiness, excitement, anger, anxiety, pain, vigilance, and attention-seeking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze uploaded pet audio or video, classify cat and dog vocal emotions, and retrieve structured analysis reports or prior report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report metadata are processed by the provider's cloud service.

Mitigation: Use the skill only with media appropriate for provider processing, and avoid sensitive recordings unless the provider's handling is acceptable.

Risk: The skill can silently create or reuse an account identity and persist tokens locally.

Mitigation: Review local identity and token storage before use, clear workspace data between users, and avoid shared workspaces for sensitive activity.

Risk: Automatic history-report lookup can retrieve account-linked prior reports.

Mitigation: Run history lookup only when needed and confirm the workspace identity belongs to the intended user before retrieving prior reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-vocal-emotion-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured analysis report text or JSON, with optional Markdown report lists and saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and account-linked historical report records returned by the provider service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
