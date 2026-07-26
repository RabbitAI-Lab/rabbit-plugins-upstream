## Description: <br>
Vaaya routes agents to an external MCP gateway for media generation, web search and scraping, document parsing, sandboxed compute, browser automation, communications, GTM workflows, and scheduled web workers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marupelkar](https://clawhub.ai/user/marupelkar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when a task needs external services that the base agent cannot perform directly, such as current web research, media generation, scraping, code execution, outbound communications, lead enrichment, or long-running monitoring. It acts as a consult-first gateway that asks Vaaya to plan and execute appropriate MCP tool calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary flags this as a broad external-capability gateway with high-impact actions and insufficient user-directed control. <br>
Mitigation: Review intended Vaaya calls before execution and confirm user intent for connected-account actions, paid services, persistent workers, outbound communications, and automation rules. <br>
Risk: The security guidance notes that the skill can use connected accounts, spend credits, create persistent workers, store or retrieve data, and perform outbound communications. <br>
Mitigation: Review MCP configuration changes, OAuth grants, billing limits, auto-send settings, automation rules, and reply-send behavior before deployment or use. <br>


## Reference(s): <br>
- [Vaaya ClawHub Skill Page](https://clawhub.ai/marupelkar/skills/vaaya) <br>
- [Vaaya MCP npm Package](https://www.npmjs.com/package/@vaaya/mcp) <br>
- [Vaaya MCP Endpoint](https://vaaya.ai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Code, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON-like tool call examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger external MCP calls that return media, files, web data, sandbox output, communications drafts, worker findings, or GTM workflow results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
