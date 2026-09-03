## Description:

Manage, orchestrate, inspect, and automate the Orca IDE and Multi-Agent Runtime Server, including projects, worktrees, supervised workers, interactive terminals, decision gates, accounts, and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and administer Orca runtime environments, coordinate multi-agent task execution, manage worktrees and terminals, and run operational diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad Orca runtime administration across services, terminals, workers, accounts, automations, and browser state.

Mitigation: Install it only for trusted Orca hosts where the agent is expected to administer the runtime.

Risk: Commands can affect accounts, service state, worktrees, decision gates, terminal sessions, automations, and browser captures.

Mitigation: Require explicit user approval before account authentication, service restarts, worktree deletion, decision-gate resolution, terminal command sending, automation runs, or browser snapshot and screenshot capture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/orca-control)
- [Orca Control source homepage](https://github.com/rafacpti23/orca-control-skill)
- [Commands cheatsheet](references/commands_cheatsheet.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational commands and checks for Orca runtime administration.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
