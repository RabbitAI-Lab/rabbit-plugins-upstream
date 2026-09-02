## Description:

A cross-session and cross-project workflow standard that helps AI agents read project state at startup, maintain nearby `.workflow` notes during work, and leave a handoff anchor at finish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and external AI-agent users use this skill to keep project status, tasks, decisions, logs, and handoff anchors consistent across sessions and across multiple agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent `.workflow` notes can capture private project context or sensitive details.

Mitigation: Avoid recording secrets or customer-sensitive details, and add `.workflow/` to `.gitignore` for private work.

Risk: Global multi-agent installation can enable the workflow behavior across more agents than intended.

Mitigation: Prefer targeted `--agent` or `--dir` installation unless the same behavior is desired across all configured agents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-workflow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-workflow)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Configuration]

**Output Format:** [Markdown project-state files and handoff-anchor text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update `.workflow` project state files when project work is in scope.]

## Skill Version(s):

0.2.6 (source: frontmatter, changelog released 2026-08-29, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
