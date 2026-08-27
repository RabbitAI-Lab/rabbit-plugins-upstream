## Description:

A cross-session, cross-project workflow standard that guides AI agents to read project state on start, maintain nearby `.workflow` Markdown state, persist logs, tasks, and decisions while working, and leave a handoff anchor on finish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and teams use this skill to keep AI agent project work resumable across sessions and across agent tools. It standardizes project-local Markdown state files and handoff anchors so agents can recover context before continuing work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent `.workflow` logs and state can capture sensitive project details if agents write too broadly.

Mitigation: Add `.workflow/` to `.gitignore` unless intentional, and instruct agents not to record secrets, credentials, private customer data, or sensitive incident details.

Risk: Global installation can make the workflow active across many agent tools and projects.

Mitigation: Prefer `--agent` or `--dir` scoped installation when broad activation is not intended; review target skill directories before using `-g`.

Risk: Shared state files can become misleading if agents rely on stale or incomplete entries.

Mitigation: Require agents to read the existing state before work, update task and decision files during work, and reconcile the handoff anchor with the state files before ending a session.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown state files and Markdown/text handoff anchors, with optional shell commands and configuration snippets for installation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local `.workflow` state when triggered; no credential environment variables, MCP tools, or API calls were detected in the provided evidence.]

## Skill Version(s):

0.2.5 (source: frontmatter, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
