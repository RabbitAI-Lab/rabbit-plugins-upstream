## Description:

Set up, inspect, or maintain a local user-preference memory shared across coding agents such as Codex and Claude Code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding-agent users use Dongwo to opt in to a local, auditable preference memory that can be loaded by Codex and Claude Code. It helps inspect, maintain, and forget stored preferences while keeping the current user request and project instructions higher priority than memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local preference memory can affect future agent context.

Mitigation: Enable hooks only after explicit user opt-in, and review `myprofile.md` plus `.dongwo/memory/` before use.

Risk: Profile or memory text may be forgeable or influenced by untrusted repository files.

Mitigation: Do not use Dongwo in repositories where untrusted files can define the profile or memory inputs.

Risk: Confidential prompts or sensitive preference evidence could remain in local memory.

Mitigation: Avoid highly confidential work unless memory files can be controlled and audited, and delete matching inbox evidence before running `consolidate` when forgetting items.

## Reference(s):

- [Dongwo skill page](https://clawhub.ai/cutd/skills/dongwo)
- [cutd publisher profile](https://clawhub.ai/user/cutd)
- [懂我记忆策略](references/memory-policy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local files and Python lifecycle hooks; generated memory context is capped by the engine before injection.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
