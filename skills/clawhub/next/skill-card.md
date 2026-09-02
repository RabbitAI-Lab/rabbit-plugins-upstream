## Description:

Suggests next actions after task completion, including explicit next-action requests, completion-triggered follow-up prompts, stall detection, and ask gates for task, PR, issue, and cleanup decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to surface appropriate follow-up choices after an agent completes work, stalls, waits on external systems, or needs a user decision. It helps route follow-up actions through prompts, task checks, and supporting skills instead of leaving completion states unresolved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger after task completion and inspect local session state, task lists, workspace planning files, and GitHub or organization data.

Mitigation: Review hook registration before deployment and install only in environments where those local and remote data checks are acceptable.

Risk: Hook debug logs may retain sensitive transcript snippets or workflow state.

Mitigation: Disable or restrict debug logging where sensitive transcripts are possible and periodically review retained log files.

Risk: The skill is an assertive workflow-orchestration helper and may surface follow-up choices beyond a simple suggestion feature.

Mitigation: Review the documented ask gates and skip conditions before use so operators understand when prompts, task checks, and follow-up routing may occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Next skill instructions](artifact/SKILL.md)
- [Stall detection topic](artifact/stall-detect.md)
- [Ask gates topic](artifact/ask-gates.md)
- [Suggestion patterns topic](artifact/suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown and structured next-action options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or route follow-up actions through available agent skills and host hooks.]

## Skill Version(s):

0.9.2 (source: server release metadata and CHANGELOG, released 2026-09-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
