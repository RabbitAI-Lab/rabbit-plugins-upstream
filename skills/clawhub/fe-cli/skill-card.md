## Description:

Scaffolds standardized frontend projects across nine web, desktop, and mobile project types, and reviews existing projects against its conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to initialize frontend applications with a selected framework and shared tooling, or to review an existing project's configuration and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated projects may contain third-party packages that are unsuitable for production needs.

Mitigation: Review dependency choices and versions before deploying a generated project.

Risk: Template API or desktop update URLs may remain as placeholders.

Mitigation: Replace placeholder endpoints with approved destinations and review desktop auto-update settings before release.

Risk: Local token persistence may expose sensitive authentication data in generated applications.

Mitigation: Choose and harden authentication storage for the application's sensitivity before production use.

Risk: The default Chinese interface locale may not match the intended audience.

Mitigation: Specify and verify the desired locale when generating a project.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/z-zihan/skills/fe-cli)
- [Declared project homepage (GitHub provenance unavailable)](https://github.com/z-Zihan/awesome-skills)
- [Shared frontend templates](artifact/references/shared-base.md)
- [Shared configuration templates](artifact/references/shared-config.md)
- [Shared application infrastructure templates](artifact/references/shared-infrastructure.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Markdown guidance]

**Output Format:** [Frontend project files and Markdown setup or review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports nine project types; generated interface text defaults to Chinese unless another locale is requested.]

## Skill Version(s):

3.1.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
