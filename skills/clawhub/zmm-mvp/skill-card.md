## Description:

Helps solo knowledge creators turn raw topic fragments into ready-to-post X text tests, log them in a testing pipeline, and use real engagement data to decide whether to expand, schedule, or discard the topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and their agents use this skill to test content ideas cheaply on X before investing time in video or long-form production. It drafts plain-text test posts, records the test in a local pipeline, and supports later data-based decisions from reported engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local ZMM vault materials and X-post history, then writes drafts, pipeline records, and workflow memory.

Mitigation: Install it only in the intended vault workspace, review generated file changes, and keep backups for workflow records.

Risk: Drafted X tests could contain unsupported claims if the source fragment lacks real evidence.

Mitigation: Use the skill's content gate and factuality checks; require real data, firsthand stories, specific pain points, or cited support before publishing.

Risk: The skill copies final post text to the clipboard for manual publishing.

Mitigation: Inspect the clipboard content before posting; the skill does not publish to X on the user's behalf.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-mvp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with plain-text X post drafts, local file paths, and occasional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save local draft files, update local pipeline records, copy final text to the clipboard, move published drafts, and write workflow memory.]

## Skill Version(s):

0.2.5 (source: server release metadata; artifact frontmatter lists 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
