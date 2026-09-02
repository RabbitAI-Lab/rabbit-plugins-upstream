## Description:

Agent Constraints helps developers decide whether an agent rule belongs in a deterministic hook or permission, AGENTS.md or CLAUDE.md, a skill, a path-scoped rule, or a one-time prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to govern coding-agent constraints, choose the right enforcement layer, trim overgrown instruction files, and set up review workflows for repeated agent failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional session hook can keep local records of project paths, session IDs, and transcript paths.

Mitigation: Enable the hook only after reviewing this logging behavior, store the log in a private location with restrictive file permissions, and clear it periodically.

Risk: Guidance for hooks, permissions, and path-scoped rules may be agent-specific and can be misapplied to unsupported clients.

Mitigation: Apply Claude Code-specific syntax only to Claude Code environments and adapt or validate equivalent controls before using the guidance with other agents.

Risk: The skill relies on preprint research and states that conclusions may not transfer across languages, models, tasks, or repositories.

Mitigation: Validate important constraints in the target repository and agent setup before treating the guidance as operational policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/snowsonz/skills/agent-constraints)
- [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988)
- [Instruction Adherence in Coding Agent Configuration Files](https://arxiv.org/abs/2605.10039)
- [Agent READMEs](https://arxiv.org/abs/2511.12884)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks, configuration snippets, shell commands, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional local session-hook setup that records project paths, session IDs, and transcript paths when enabled.]

## Skill Version(s):

0.1.3 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
