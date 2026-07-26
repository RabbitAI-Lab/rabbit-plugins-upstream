## Description: <br>
A prompt-generation skill that calls XiaoBenYang's remote MCP service to assemble PRD, codebase analysis, and bug analysis prompts and Markdown templates for AI assistants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to generate PRD prompts, codebase analysis prompts, bug analysis prompts, and standard Markdown templates from selected technology stacks and analysis focus areas. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided project, PRD, codebase, or bug context to a third-party remote service. <br>
Mitigation: Use it only when XiaoBenYang is approved for the data being shared, and avoid confidential code or business details unless that service is acceptable for the use case. <br>
Risk: The skill requires an XBY_APIKEY and can persist it to a local .env file. <br>
Mitigation: Prefer a managed environment or secret store for XBY_APIKEY, keep .env out of version control, and rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/generate-prd-prompt) <br>
- [XiaoBenYang API key service](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown and structured text derived from remote API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY and may use user-provided project, codebase, PRD, or bug context in requests to the remote service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
