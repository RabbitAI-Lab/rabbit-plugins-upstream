## Description:

Detects and recognizes cats and dogs from smart-feeder or IPC camera images and videos, supports pet identity matching and enrollment, and returns structured reports for smart feeding scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to analyze smart feeder or IPC camera media for pet detection, cat/dog classification, identity recognition, pet enrollment, and report-history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded local files or provided media URLs may be processed by an external cloud service.

Mitigation: Use only media that is appropriate for cloud processing, and avoid sensitive home camera footage unless that processing is acceptable.

Risk: The skill creates or reuses a local identity and stores account tokens in a workspace SQLite database.

Mitigation: Protect the workspace data directory, review local account storage before deployment, and clear or rotate stored credentials when changing accounts.

Risk: History lookup can automatically retrieve cloud report records linked to the local identity.

Mitigation: Run history queries only in contexts where exposing the linked account's report history to the agent and user is expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet detection API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, shell commands, guidance]

**Output Format:** [Markdown-style structured reports and JSON strings; optional saved text output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and structured history-report lists.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
