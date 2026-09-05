## Description:

Rebuild full working context at the start of any session after a context reset.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill at session start or after an interruption to reload durable memory, active task state, and project source-of-truth documents, then produce a concise, source-verified resume brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace memory files and project notes may contain private work context.

Mitigation: Use the skill only in appropriate workspaces and keep sensitive secrets out of memory documents.

## Reference(s):

- [Context Resume ClawHub listing](https://clawhub.ai/tooled-app/skills/context-resume)
- [IKKF](https://ikkf.info)
- [Tooled](https://tooled.pro)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown brief with concise bullets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims should trace to files read in the current session; unverified context is flagged.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
