## Description: <br>
Moderate text, images, and video using Vettly's content moderation API via MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[code-with-brian](https://clawhub.ai/user/code-with-brian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and moderation operators use this skill to check user-generated text, image, and video content against Vettly policies, validate policy YAML, audit recent moderation decisions, and monitor usage or cost trends. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on Vettly and the @vettly/mcp npm package, so users inherit external-service and package trust considerations. <br>
Mitigation: Install only when Vettly and the package are approved for the environment; pin a known-good package version where supported. <br>
Risk: Moderation requests may send content or media URLs to Vettly. <br>
Mitigation: Use a least-privileged Vettly API key and avoid sending secrets, regulated personal data, or private signed media URLs unless Vettly is approved for that data. <br>


## Reference(s): <br>
- [ClawHub Content Moderation Skill](https://clawhub.ai/code-with-brian/skills/content-moderation) <br>
- [Vettly](https://vettly.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown with JSON configuration snippets and moderation result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a VETTLY_API_KEY environment variable and npx to run the Vettly MCP server.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
