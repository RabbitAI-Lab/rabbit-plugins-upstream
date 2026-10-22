## Description:

Counts characters, words, lines, word frequency, and estimated reading time in text files or directories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and developers use this skill to check document length, common words, and reading time for a file or a batch of files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The permission declarations understate the local file reading and process execution needed by the skill.

Mitigation: Run only on files or directories you explicitly choose; ask the publisher to disclose filesystem and subprocess use before treating the permissions as accurate.

Risk: The manifest grants an unnecessary Write tool permission.

Mitigation: Remove the Write permission before deploying the skill with least-privilege access.

## Reference(s):

- [Text Stats on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/text-stats)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports file count, character count, word count, line count, estimated reading minutes, and top word frequencies.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
