## Description:

This skill analyzes plant leaf images or videos to identify likely nutrient deficiencies, confidence scores, and fertilization direction guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, gardening assistants, and agricultural operators use this skill to evaluate plant leaf media for likely nutrient deficiencies and receive concise diagnostic results, confidence information, and fertilization direction guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs may be sent to Lifeemergence-hosted services for analysis.

Mitigation: Use only with media the user is comfortable uploading, and confirm the publisher's data retention, deletion, and consent practices before deployment.

Risk: Report history is associated with an automatically created or reused identity.

Mitigation: Review user identity handling and history retrieval behavior before enabling the skill in shared or regulated environments.

Risk: Local token-bearing state may be stored in the workspace data directory.

Mitigation: Limit workspace access, rotate or delete local state when users change, and review token handling expectations before installation.

Risk: Plant nutrient symptoms can overlap, so diagnostic output may be uncertain or incomplete.

Mitigation: Treat results as advisory and combine them with plant species context, image quality checks, soil testing, or expert review for high-impact decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with structured analysis results, confidence information, suggestions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file and can return history reports as Markdown tables.]

## Skill Version(s):

1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
