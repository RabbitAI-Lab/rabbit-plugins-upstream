## Description:

Daily standup meeting assistant - collect updates, generate summary, and distribute to the team channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and team leads use this skill to run asynchronous daily standups by collecting member updates, synthesizing blockers and action items, posting a summary to a team channel, and preserving a searchable archive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standup updates may include private, sensitive, or premature team information that is posted or archived.

Mitigation: Tell participants where updates are collected, who can see summaries, what is archived, and how to redact sensitive information before submission.

Risk: Broad messaging gateway permissions could expose standup collection or summaries beyond the intended team.

Mitigation: Use a dedicated standup channel and restrict gateway permissions to only the channels, members, and storage locations needed for the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/daily-standup)
- [ClawHub publisher profile](https://clawhub.ai/user/terrycarter1985)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown summaries with structured status, blockers, action items, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write dated standup archive files and update team memory when configured.]

## Skill Version(s):

1.0.0 (source: server release evidence, artifact metadata, and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
