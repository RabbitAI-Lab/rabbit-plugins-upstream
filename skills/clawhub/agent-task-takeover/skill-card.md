## Description:

Take over, review, resume, or hand off AI coding tasks by locating and safely reading conversation records across CLI and desktop agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lawson2019](https://clawhub.ai/user/lawson2019)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review or continue work from another coding agent's conversation, or prepare a clear handoff for another agent. It helps locate supported local session stores, reconstruct task state, redact transcript output, and verify handoff details against files on disk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install examples do not pin a release version.

Mitigation: Pin the release version when installing and verify the package publisher before use.

Risk: The benign security verdict has medium confidence; coverage was partial (11 of 12 components scanned) and one analysis was degraded.

Mitigation: Review the package source and relevant files before relying on the skill, especially when handling sensitive local session data.

## Reference(s):

- [Agent session store guide](references/agent-stores.md)
- [ClawHub release page](https://clawhub.ai/lawson2019/skills/agent-task-takeover)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Files, Shell commands]

**Output Format:** [Markdown task summaries and handoff notes, with shell command examples where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript-derived material may be redacted; output depends on locally available session data.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
