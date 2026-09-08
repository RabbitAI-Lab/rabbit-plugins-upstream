## Description:

Classifies shell commands as SAFE, WARN, or CRIT before execution and documents optional OpenClaw patch scripts that can enable plugin-level tool-call blocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to classify shell commands before an AI agent runs them and to surface warnings for commands that could modify state or cause damage. OpenClaw users may also inspect and run the optional patch scripts to enable plugin-level tool-call blocking in a local checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt-level command classification can be bypassed by model error, prompt injection, or a determined jailbreak.

Mitigation: Treat the SAFE/WARN/CRIT gate as guidance, review high-impact commands manually, and run agents in containers or VMs when hard isolation is required.

Risk: The optional patch script modifies a TypeScript file in an OpenClaw checkout and can run that checkout's build scripts if --rebuild is used.

Mitigation: Read the scripts before use, run --dry-run first, keep the target checkout under version control, avoid --allow-any-repo unless intentional, and rebuild only after reviewing the target project.

Risk: Terminal-formatted command output can be spoofed, and command arguments may expose secrets through process tables or shell history.

Mitigation: Do not pass secrets through cmd_display.py arguments and be cautious when displaying untrusted command output in a terminal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/shell-security-ultimate)
- [Project referenced by the skill documentation](https://github.com/globalcaos/clawdbot-moltbot-openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and optional terminal-formatted status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces prompt-level command classifications; optional helper scripts require deliberate local execution.]

## Skill Version(s):

2.3.1 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
