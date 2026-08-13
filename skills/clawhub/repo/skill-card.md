## Description:

Project initialization toolkit that helps agents generate a CONTRIBUTING.md guide from detected project structure and configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to inspect project configuration and produce a project-specific CONTRIBUTING.md guide. It is intended for repository setup and contribution workflow documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases such as init may activate the skill when the user only meant to discuss project setup.

Mitigation: Use specific prompts for CONTRIBUTING.md generation and confirm intent before writing repository documentation.

Risk: Generated contribution guidance may not match the project's intended conventions or language.

Mitigation: Review the generated CONTRIBUTING.md before accepting it and specify the desired output language when it matters.

## Reference(s):

- [Contributing Generator guide](contributing.md)
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/repo)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a CONTRIBUTING.md draft and asks before overwriting an existing file.]

## Skill Version(s):

0.3.1 (source: server release metadata and changelog, released 2026-08-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
