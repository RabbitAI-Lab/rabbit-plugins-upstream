## Description:

Installs, updates, repairs, and connects the Rainskills runtime and its bundled Rainbond agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuzhonglin12138](https://clawhub.ai/user/xuzhonglin12138)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and maintain the Rainskills agent suite, then connect a Rainbond environment for deployment and operations tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and later package updates can replace installed Rainbond agent skills.

Mitigation: Install only from a trusted publisher and review updates before allowing them to refresh skills.

Risk: The suite stores protected state and Rainbond credentials locally and sends anonymous telemetry by default.

Mitigation: Protect access to ~/.rainbond and use --no-telemetry if telemetry is not acceptable.

## Reference(s):

- [ClawHub Rainskills release](https://clawhub.ai/xuzhonglin12138/skills/package)
- [RainSkills installation and use](https://www.rainbond.com/docs/ai/rainskills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installs separate Rainbond agent skills and reports setup or connection status.]

## Skill Version(s):

1.0.0 (source: ClawHub release; bundled npm package: 0.1.43)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
