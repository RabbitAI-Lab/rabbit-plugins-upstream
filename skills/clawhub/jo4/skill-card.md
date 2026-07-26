## Description: <br>
URL shortener, QR code generator, and link analytics API. Create short links, generate QR codes, and track click analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anandrathnas](https://clawhub.ai/user/anandrathnas) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, marketers, and operations teams use this skill to create short links and QR codes, manage link metadata, and inspect click analytics for shared URLs and campaigns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Jo4 API key for protected operations. <br>
Mitigation: Use a revocable or dedicated API key and keep it in the JO4_API_KEY environment variable rather than embedding it in prompts or files. <br>
Risk: Link analytics can include privacy-sensitive click, device, browser, geography, and referrer information. <br>
Mitigation: Review analytics outputs according to the user's privacy and data-handling requirements before sharing or storing them. <br>
Risk: Update and delete operations can change or remove existing short links. <br>
Mitigation: Require explicit confirmation before modifying or deleting links, especially links already shared publicly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anandrathnas/skills/jo4) <br>
- [Jo4 website](https://jo4.io) <br>
- [Jo4 API documentation](https://jo4-api.jo4.io/swagger-ui/index.html) <br>
- [Jo4 API keys](https://jo4.io/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with curl command examples and JSON request and response snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JO4_API_KEY for protected operations; anonymous short-link creation has limited features and no analytics access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
