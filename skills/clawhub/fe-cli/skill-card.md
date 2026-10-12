## Description:

Scaffolds frontend projects across nine web, desktop, and mobile project types and can review existing projects against its conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to initialize React, Vue, and related frontend projects with shared configuration, or to audit an existing project's structure and conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scaffolding runs package-manager commands and installs project dependencies.

Mitigation: Review commands and dependencies before running them in the project directory.

Risk: Generated authentication and token-storage defaults may not suit sensitive applications.

Mitigation: Review credential handling and replace unsuitable defaults before production use.

Risk: Generated local logs may retain sensitive data.

Mitigation: Review logging content, storage, and export settings before handling sensitive data.

Risk: Optional desktop auto-update endpoints and deployment steps require project-specific configuration.

Mitigation: Verify update endpoints and deployment commands before enabling or running them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/z-zihan/skills/fe-cli)
- [Publisher-listed skill homepage](https://github.com/z-Zihan/awesome-skills)
- [Shared frontend templates](artifact/references/shared-base.md)
- [Shared configuration templates](artifact/references/shared-config.md)
- [Shared infrastructure templates](artifact/references/shared-infrastructure.md)
- [AI-readable project documentation template](artifact/references/ai-project-md.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Markdown, Guidance]

**Output Format:** [Generated project files and Markdown setup or audit guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates an AI-readable project guide and can report gaps in existing projects.]

## Skill Version(s):

3.1.3 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
