## Description:

AI KEY·选题先试水 helps a solo knowledge creator turn rough topic fragments into plain-text X test posts, log the test pipeline, and use engagement data to decide whether to expand, adapt, or discard the topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Solo knowledge creators use this skill to cheaply validate content topics on X before spending time on video production. The agent drafts candidate X posts, records test workflow state, and helps interpret engagement signals for next-step decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local AI KEY reference and memory files and a local CSV of X posts.

Mitigation: Install only where those local files are intended to be available to the agent, and review the data sources before use.

Risk: The skill may write draft and pipeline records and overwrite the clipboard with finalized post text.

Mitigation: Review generated drafts and local file changes before manually posting or reusing the copied text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/aikey-mvp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text and Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local draft and pipeline records and copy finalized post text to the clipboard when used in the described local vault workflow.]

## Skill Version(s):

0.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
