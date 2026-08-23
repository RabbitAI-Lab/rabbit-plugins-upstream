## Description:

Classifies pet vocalization audio or video into emotion categories with confidence scores and returns structured reports and report links without providing medical or behavior-modification advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze pet vocalization media or URLs, classify likely emotional states, and retrieve prior cloud-generated reports for the same locally associated identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media files or media URLs are sent to a configured cloud service for analysis.

Mitigation: Use only non-sensitive media or public URLs unless the publisher documents endpoint ownership, retention, deletion, and account-linkage controls.

Risk: The skill creates or reuses a local identity and token database in the workspace.

Mitigation: Review local data creation before installation and avoid sharing workspaces that may contain generated identity or token state.

Risk: History retrieval can expose prior cloud reports associated with the local identity.

Mitigation: Use the history feature only in contexts where report linkage is expected, and clear or isolate local identity state when switching users or projects.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocal-emotion-classification-analysis)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON report text, with optional saved output file and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [History queries return cloud report records; analysis output may include confidence scores, structured results, and a cloud report export link.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
