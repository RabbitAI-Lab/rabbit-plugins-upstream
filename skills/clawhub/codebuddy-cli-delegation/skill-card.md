## Description:

Guides developers in delegating large coding batches to a headless CodeBuddy CLI agent with a clean-environment launcher, scoped instructions, and independent acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carloswonmore](https://clawhub.ai/user/carloswonmore)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to delegate lengthy repository changes, tests, or documentation batches to CodeBuddy CLI and independently verify the resulting work. Its launcher and command guidance are specific to CodeBuddy CLI, not other coding agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended child-agent work may change unintended repository files.

Mitigation: Use a clean or separate worktree, restrict file and tool scope, review diffs, and rerun tests independently.

Risk: Prompts and stored run logs may expose secrets.

Mitigation: Keep secrets out of prompts and .cli-runs logs.

Risk: Automatic child-CLI approval can permit unsafe actions.

Mitigation: Do not treat bypassPermissions as approval to push, force-reset, delete data, or touch production without explicit authorization.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/carloswonmore/skills/codebuddy-cli-delegation)
- [Server-resolved source repository](https://github.com/CarlosWonMore/codebuddy-cli-delegation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a CodeBuddy CLI launcher template and independent review checklist.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
