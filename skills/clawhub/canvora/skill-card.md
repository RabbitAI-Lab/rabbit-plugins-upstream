## Description: <br>
Canvora helps agents create on-brand visuals such as social posts, carousels, decks, ads, and documents from text, URLs, or PDFs through the Canvora CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[canvora](https://clawhub.ai/user/canvora) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and agent operators use this skill to select Canvora formats, brand kits, input modes, and CLI commands for generating or refining visual content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Content sent through URL, file-url, or input modes may be processed by Canvora. <br>
Mitigation: Do not use those modes with confidential, internal, or customer-sensitive material unless the user intends to send that content to Canvora. <br>
Risk: CANVORA_API_KEY exposure could allow unauthorized use of the Canvora account. <br>
Mitigation: Keep the API key out of logs, screenshots, shared scripts, and generated examples. <br>
Risk: Regenerating after a timeout can create a new paid generation. <br>
Mitigation: Use canvora status with the existing generation ID instead of rerunning generate after a timeout. <br>
Risk: Large or repeated jobs can consume paid credits quickly. <br>
Mitigation: Check canvora credits --json before large jobs and account for per-visual and per-slide costs. <br>


## Reference(s): <br>
- [Canvora ClawHub skill page](https://clawhub.ai/canvora/skills/canvora) <br>
- [Canvora publisher profile](https://clawhub.ai/user/canvora) <br>
- [Canvora MCP server](https://api.canvora.ai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Canvora CLI commands should use --json; generated results include output URLs and metadata from the Canvora service.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
