## Description:

Reads workspace text files and generates concise summaries for logs, reports, CSVs, and multi-line content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muhammadmuazzain](https://clawhub.ai/user/muhammadmuazzain)

### License/Terms of Use:


## Use Case:

Developers and other ClawHub users use this skill to summarize local text files such as logs, reports, notes, and CSVs into brief human-readable summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The implementation can read outside the declared workspace despite claiming path traversal is blocked.

Mitigation: Review before installing, avoid sensitive local files, and require path containment before trusting the skill with broader file access.

Risk: Broad triggers may activate the skill for requests that are not explicit file-summarization tasks.

Mitigation: Narrow triggers to explicit file-summarization intents and review execution before deployment.

## Reference(s):

- [Summarize File on ClawHub](https://clawhub.ai/muhammadmuazzain/skills/summarize-file)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a concise local-file summary; runtime behavior may return truncated file content rather than a synthesized summary.]

## Skill Version(s):

1.0.0 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
