## Description:

Classifies shell commands as SAFE, WARN, or CRIT before agent execution and ships optional helpers for terminal display and OpenClaw hook patching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators giving an agent shell access use this skill to classify proposed commands, surface risky actions before execution, and optionally prepare an OpenClaw checkout for hook-based blocking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SAFE/WARN/CRIT gate is advisory instruction-level behavior by default and can be bypassed by misclassification or prompt injection.

Mitigation: Review classifications before execution and use a container, VM, or other isolation when hard enforcement is required.

Risk: The optional patch script modifies source code in an OpenClaw checkout selected by the user.

Mitigation: Read and dry-run the patch script first, set OPENCLAW_DIR deliberately, require explicit consent, and use the bundled unpatch script to revert.

Risk: Command-line arguments passed to the display helper can appear in process listings or shell history.

Mitigation: Do not pass secrets through display helper arguments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/shell-security-ultimate)
- [Project repository](https://github.com/globalcaos/clawdbot-moltbot-openclaw)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with terminal text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional helper scripts are run deliberately by the user; the display helper sanitizes and length-caps printed arguments.]

## Skill Version(s):

2.3.2 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
