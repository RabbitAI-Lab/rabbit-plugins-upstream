## Description:

Implements GitHub or GitLab issues via parallel subagents with review gates between task batches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use do-issue to turn one or more GitHub or GitLab issues into an implementation plan, dispatch parallel or sequential agents, run review gates, and prepare a consolidated pull request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write remote issue comments or close issues while resolving work.

Mitigation: Use explicit issue numbers, review generated comments before posting, and keep issue closure disabled unless closure is intentionally approved.

Risk: The skill includes an external tooling-feedback step that can send observations to the Night Market GitHub Discussions repository.

Mitigation: Disable or ignore that feedback step unless the user explicitly wants tooling observations sent outside the current project.

Risk: Parallel subagents can make code changes and commits that conflict or miss requirements.

Mitigation: Run dependency and conflict analysis before dispatch, limit broad parallel batches, and require review gates plus tests before preparing a pull request.

Risk: Subagent-heavy runs may hang in remote-control or headless sessions.

Mitigation: Prefer local execution for subagent-heavy workflows, limit concurrency, and use background-capable execution when remote monitoring is necessary.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-sanctum-do-issue)
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, task plans, code changes, and issue or pull request text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use platform CLIs and subagents to fetch issues, edit code, commit changes, update issue comments, and prepare one consolidated pull request.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
