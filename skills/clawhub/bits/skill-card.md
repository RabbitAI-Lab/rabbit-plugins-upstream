## Description: <br>
Control browser automation agents via the Bits MCP server for web scraping, form filling, data extraction, and browser-based automation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbiethompson18](https://clawhub.ai/user/robbiethompson18) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation operators use this skill to connect an AI assistant to the Bits MCP server for browser navigation, scraping, form interaction, authentication flows, and structured data extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automate actions on real websites and accounts, including authenticated flows and state-changing interactions. <br>
Mitigation: Confirm tasks before using the skill on real accounts, OAuth or 2FA flows, purchases, messages, admin panels, or other sensitive workflows. <br>
Risk: The MCP configuration uses a Bits API key and launches an npm package. <br>
Mitigation: Install only if the Bits service and npm package are trusted, keep BITS_API_KEY private, avoid committing MCP config files, and rotate or revoke exposed keys. <br>


## Reference(s): <br>
- [Bits API OpenAPI Specification](https://api.usebits.com/openapi.json) <br>
- [Bits Web App](https://app.usebits.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/robbiethompson18/skills/bits) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, Code, JSON] <br>
**Output Format:** [Markdown with JSON configuration examples, shell commands, and TypeScript code guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured JSON extraction results from browser automation tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
