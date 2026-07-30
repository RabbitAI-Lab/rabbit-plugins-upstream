## Description: <br>
Use configured SandBase MCP tools to discover available SandBase capabilities, retrieve live information, create content, or complete SandBase-backed workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joeliu926](https://clawhub.ai/user/joeliu926) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they want an agent to select and invoke configured SandBase MCP tools for live information retrieval, content creation, or SandBase-backed workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates work to whichever SandBase MCP tools are configured, so tool permissions may exceed the skill text itself. <br>
Mitigation: Review the configured SandBase MCP server permissions and available tools before installation or use. <br>
Risk: SandBase may be unavailable, misconfigured, or return a failed tool result. <br>
Mitigation: Report meaningful failures and avoid fabricating results or silently switching providers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/joeliu926/skills/sandbase) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/joeliu926) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown or plain text, depending on the selected SandBase workflow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output depends on the configured SandBase MCP tools available in the user's environment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
