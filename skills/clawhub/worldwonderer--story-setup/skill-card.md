## Description:

Deploys and checks a web fiction writing toolkit across supported agent environments, using host-specific setup or a generic file-based configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and project maintainers use the skill to deploy, update, or diagnose an AI-assisted web fiction writing workspace across supported agent tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with high confidence and reports shell command injection risk and unsafe installation guidance. Its scan was partial, so some behavior is not fully assessed.

Mitigation: Review shell-based search handling and installation steps before deploying, verify the project folder, and keep a recoverable copy of existing project configuration.

Risk: The security assessment says behavior extends beyond the described setup and checking purpose, including writing checks, external research, and browser interaction.

Mitigation: Use check-only mode for diagnostics, and review the selected host's deployment instructions and any research or browser actions before proceeding.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/worldwonderer/skills/story-setup)
- [Repository link in OpenClaw metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Deployment and recovery guidance](references/deploy-generic.md)
- [Environment diagnostics](references/diagnostics.md)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Code, Guidance]

**Output Format:** [Project configuration files, Markdown instructions, and setup or diagnostic guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The selected host and project determine which configuration files and guidance are produced.]

## Skill Version(s):

1.2.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
