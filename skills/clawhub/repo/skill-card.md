## Description:

Project initialization toolkit that helps generate CONTRIBUTING.md guidance from detected project structure and configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and maintainers use this skill to inspect repository structure and common project configuration, then draft a CONTRIBUTING.md file that reflects the project settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic project initialization or contributing-guide requests may invoke this skill when a narrower workflow was intended.

Mitigation: Confirm the requested repository documentation task before applying generated guidance.

Risk: Generated CONTRIBUTING.md content may not match a repository's required language, wording, or policy.

Mitigation: Review the generated file before accepting it, especially for project-specific language and contribution policies.

## Reference(s):

- [Contributing Generator guide](artifact/contributing.md)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates repository contribution guidance for human review before acceptance.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
