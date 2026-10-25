## Description:

Reviews academic papers against their source text, prepares research notes, and supports evidence-based evaluation and deep reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangzw928](https://clawhub.ai/user/wangzw928)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and research assistants use this skill to assess papers, explain methods and limitations, and prepare source-grounded reading notes. With authorization, it can organize notes in a research repository and update its deep-reading index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paper text and notes may be processed by Codex with access to inherited environment variables.

Mitigation: For confidential manuscripts, use an isolated workspace with a scrubbed environment and confirm that the material can be shared before processing.

Risk: Generated notes, review receipts, or index edits may contain mistakes or unintended changes.

Mitigation: Check the notes against the source and review receipts, index changes, and the Git diff before authorizing a commit or push.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Source-grounded paper assessments and Markdown reading notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update a research index when archiving; commits and pushes require user authorization.]

## Skill Version(s):

1.0.7 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
