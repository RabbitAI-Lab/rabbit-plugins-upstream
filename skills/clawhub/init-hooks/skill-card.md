## Description:

Manages persistent OpenClaw startup hooks, including inline commands, local scripts, and remote packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use the skill to install, create, order, test, and manage startup hooks that persist across OpenClaw gateway or container restarts. It also helps synchronize OpenClaw configuration to configured persistence paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the skill suspicious and reports an archive extraction path escape, undeclared configuration changes, and broad triggers that may run or synchronize hooks on ambiguous requests; its analysis is incomplete.

Mitigation: Review the suspicious verdict and DO_NOT_INSTALL recommendation before installing. Inspect archive contents and configuration changes, verify remote downloads with SHA-256, and require clear user intent before installing or running hooks.

## Reference(s):

- [ClawHub init-hooks release](https://clawhub.ai/songhonglei/skills/init-hooks)
- [Hook authoring best practices](references/best-practices.md)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, shell commands, Python or shell scripts, and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update startup hook registrations, logs, downloaded hook files, and OpenClaw configuration copies.]

## Skill Version(s):

1.0.1 (source: server-resolved release, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
