## Description: <br>
A demonstration MCP-style service for injecting advertising into LLM responses to show the risk of advertising-injection middleware. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers can use this skill to examine how a third-party service may forward prompts or source code and return responses that include advertising-injection behavior. It is best treated as a demonstration of middleware risk rather than a production assistant capability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may persist an API key in a local .env file. <br>
Mitigation: Use a dedicated low-privilege key where possible, rotate it regularly, and remove it from .env when the skill is no longer needed. <br>
Risk: Prompts or source code provided to the skill may be sent to a third-party service. <br>
Mitigation: Do not submit secrets, proprietary source, personal data, or other sensitive material unless the publisher and upstream service are trusted for that data. <br>
Risk: The security verdict is suspicious because evidence indicates mismatched identities and behavior users may not expect. <br>
Mitigation: Review the publisher, required API endpoint, and expected data flow before installation or use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/advertising-analysis) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, guidance] <br>
**Output Format:** [Markdown summaries of JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are derived from a third-party API and may require prompts, source code, and an API key to be provided by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
