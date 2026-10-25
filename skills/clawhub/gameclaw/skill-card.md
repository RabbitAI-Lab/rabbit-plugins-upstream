## Description:

Install, update, and launch GameClaw terminal games on supported macOS, Linux, and Windows systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arcobalneo](https://clawhub.ai/user/arcobalneo)

### License/Terms of Use:

MIT-0

## Use Case:

Players and their agents use this skill to identify supported GameClaw games and platforms, install or update game binaries without deleting saves, and troubleshoot download failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hosts-file repair can change system-wide DNS behavior.

Mitigation: Require explicit approval, review the proposed changes, back up the hosts file, and provide restoration steps before editing.

Risk: A fallback mirror can deliver an untrusted executable.

Mitigation: Use mirrors only with explicit approval; review the download source and independently verify the binary before running it.

## Reference(s):

- [GameClaw on ClawHub](https://clawhub.ai/arcobalneo/skills/gameclaw)
- [GameClaw releases](https://github.com/Arcobalneo/gameclaw/releases/latest)
- [GitHub520 hosts project](https://github.com/521xueweihan/GitHub520)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash and PowerShell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-specific installation and update steps; game launch instructions.]

## Skill Version(s):

2.0.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
