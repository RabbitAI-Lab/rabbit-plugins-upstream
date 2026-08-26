## Description:

This skill helps agents generate enterprise Word and PDF documents from Markdown across contracts, HR, sales, project, operations, technical, legal, and reporting formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaobod1](https://clawhub.ai/user/zhaobod1)

### License/Terms of Use:

MIT

## Use Case:

Developers, employees, and external ClawHub users can use this skill to create structured business documents as Word files, native PDFs, or Word-to-PDF conversions. It is best suited for drafting and formatting documents that will still receive human review before business, legal, or external use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports under-disclosed credential, network, and persistent agent-configuration behavior.

Mitigation: Review before installation; use --company-name and --logo-path or --no-odoo when Odoo credential reads and network calls are not intended.

Risk: The bundled generate-config.sh script can create OpenClaw profile, workspace, and memory files.

Mitigation: Run generate-config.sh only in a controlled workspace and only when persistent OpenClaw configuration changes are desired.

Risk: Bundled contracts and deployment documents may contain draft or real-looking business details.

Mitigation: Treat generated and bundled documents as drafts; replace company details and get legal or security review before external use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-openclaw-office-doc)
- [Template usage guide](artifact/templates/README.md)
- [Skill source documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands and generated Word or PDF document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read local company profile data and may use optional Odoo fallback behavior unless explicit company inputs or --no-odoo are used.]

## Skill Version(s):

7.9.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
