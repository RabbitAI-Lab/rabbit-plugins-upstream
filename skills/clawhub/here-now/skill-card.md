## Description:

here.now lets agents publish websites and files to live URLs in seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adamludwin](https://clawhub.ai/user/adamludwin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use here.now to publish files, folders, websites, and Drive content to live URLs, manage site access, and work with team workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected files to here.now and manage private Drive content, which may expose sensitive workspace files if used on the wrong paths.

Mitigation: Review selected files and folders before publishing or uploading, avoid sensitive directories, and use narrow Drive share scopes.

Risk: The skill can keep a here.now API key on the machine for persistent authenticated publishing and Drive operations.

Mitigation: Use this only on trusted machines, consider shared-workspace implications, and rotate or remove ~/.herenow/credentials when access should end.

## Reference(s):

- [here.now docs](https://here.now/docs)
- [here.now OpenAPI schema](https://here.now/openapi.json)
- [ClawHub skill page](https://clawhub.ai/adamludwin/skills/here-now)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, URLs, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live site URLs, claim links, access-control settings, and Drive token guidance.]

## Skill Version(s):

1.28.0 (source: server release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
