## Description:

Turns a creator's topic fragment into a publish-ready X text post, records it in a testing pipeline, and uses engagement data to decide whether the idea should become a Douyin video, a longer article, or be dropped.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External knowledge creators or creator-support agents use this skill to test topic ideas cheaply as X text posts before investing time in video production or long-form expansion. It supports drafting, pipeline registration, and later engagement-based triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads fixed local creator reference and history paths that may contain sensitive material.

Mitigation: Review the configured vault paths before use and run the skill only against the intended local creator workspace.

Risk: The workflow can write draft and tracking files and replace clipboard contents.

Mitigation: Review generated text and target paths before publishing, and keep backups or version control for the local vault.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-mvp)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text X post drafts, Markdown draft and tracking entries, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local draft and tracking files and replace clipboard contents when used in the expected local vault workflow.]

## Skill Version(s):

0.2.3 (source: server release metadata; artifact frontmatter reports 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
