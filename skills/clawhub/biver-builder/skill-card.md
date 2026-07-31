## Description: <br>
Manage Biver landing pages, sections, products, forms, gallery assets, subdomains, custom domains, workspace settings, analytics, checkout data, and AI generation through the authenticated Biver API or MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramaaditya49](https://clawhub.ai/user/ramaaditya49) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and workspace operators use this skill to let an agent inspect or manage a Biver workspace through authenticated MCP or REST calls. It supports page, section, product, form, gallery, domain, workspace, analytics, checkout, and AI-generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Biver API key can affect the workspace attached to that key. <br>
Mitigation: Use the narrowest API-key scopes possible, start with read-only scopes, store the key in the client secret store, and avoid the all scope unless deliberate administration is required. <br>
Risk: Deletes, publishing, domain changes, gallery deletion, and workspace settings changes can have visible or destructive effects. <br>
Mitigation: State the exact target and impact, obtain explicit user confirmation, and set MCP confirmation only for the confirmed resource and action. <br>
Risk: Credential handling mistakes could expose the Biver API key. <br>
Mitigation: Send the key only in an authorization header or X-API-Key header, use one authentication header per request, and never place the key in a URL, file, prompt, log, or response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ramaaditya49/skills/biver-builder) <br>
- [Biver Builder source homepage](https://github.com/RamaAditya49/biver-builder) <br>
- [Biver live REST contract](https://api.biver.id/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Authenticated operations require a Biver API key; high-impact changes require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
