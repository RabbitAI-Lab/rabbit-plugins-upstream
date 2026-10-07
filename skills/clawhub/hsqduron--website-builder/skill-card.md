## Description:

Helps build, modify, and troubleshoot SaaS websites, including pages, templates, content, and forms, with optional updates to a user-authorized site.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hsqduron](https://clawhub.ai/user/hsqduron)

### License/Terms of Use:

MIT-0

## Use Case:

Website owners and developers use this skill to plan and create pages, migrate permitted public site content, build forms, and manage product and article content on an authorized SaaS website.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, deletion, batch imports, or database changes can persist on the target website.

Mitigation: Review each proposed write or deletion and its target before confirming; verify the resulting site state.

Risk: Site credentials could expose unintended websites if reused or disclosed.

Mitigation: Provide only the intended site's MCP address and site-specific Bearer token; do not expose the token in generated content.

Risk: Generated forms may collect personal details or file uploads.

Mitigation: Check collected fields and add appropriate privacy notices before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/hsqduron/skills/website-builder)
- [MCP tools reference](references/mcp-tools.md)
- [Page and template reference](references/AIPage.md)
- [Custom form reference](references/customform-democode-base.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Markdown with HTML, CSS, JavaScript, and template code as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update an authorized site when supplied with its site-specific MCP address and token.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; source file lists 1.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
