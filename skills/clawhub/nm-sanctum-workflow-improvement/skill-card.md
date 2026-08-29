## Description:

Evaluates and improves skills, agents, commands, and hooks after a workflow slice

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill after a workflow slice to evaluate friction in skills, agents, commands, and hooks, then plan and implement bounded improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can normalize creating GitHub issues and posting tooling learnings to an external repository.

Mitigation: Use it only in repositories where external issue and discussion posting is acceptable, and require preview plus explicit approval before posting.

Risk: Workflow notes or issue bodies may contain private or sensitive project details.

Mitigation: Apply a redaction and consent step before issue bodies or discussion posts are shared externally; avoid private or sensitive work unless external sharing is opt-in.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-workflow-improvement)
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or modify workflow assets and may draft issue or discussion content when configured for external tracking.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
