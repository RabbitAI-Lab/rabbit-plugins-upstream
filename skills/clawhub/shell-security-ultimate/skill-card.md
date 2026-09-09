## Description:

Classifies shell commands as SAFE, WARN, or CRIT before an agent runs them and includes optional, user-run helpers for displaying classifications and enabling OpenClaw hook-based blocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to label proposed shell commands by risk before granting shell execution. It helps them decide when a command can proceed, needs extra review, or should be blocked through an external enforcement path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt-level command classification is not a hard execution boundary.

Mitigation: Use OS, container, VM, or tool-hook enforcement for commands that require a hard block, and treat the skill's labels as decision support unless code-level blocking is separately installed.

Risk: The optional OpenClaw patch script modifies source code in a checkout selected by the user.

Mitigation: Read the patch script first, run it with --dry-run, confirm the target checkout, keep the generated backup, and use the provided unpatch script if the hook support is no longer wanted.

Risk: Command text or results passed to cmd_display.py as arguments may expose secrets through process tables or shell history.

Mitigation: Do not pass secrets, tokens, or credential-bearing command output through the display helper arguments.

Risk: Running the optional patch script with --rebuild executes build scripts from the target checkout.

Mitigation: Review the target checkout and run rebuilds only in an environment where executing that project's package scripts is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/shell-security-ultimate)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional terminal status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-level classification by default; optional helper scripts run only when deliberately invoked.]

## Skill Version(s):

2.3.2 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
