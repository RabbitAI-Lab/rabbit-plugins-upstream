## Description: <br>
Chukonu Web Search helps agents use the Chukonu remote MCP service to retrieve web, academic, and patent evidence and run deeper research for claim checking, PDF review, coverage assessment, and multi-turn investigations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hhhwor](https://clawhub.ai/user/hhhwor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when an agent needs current, citable search evidence, source-quality checks, patent or academic discovery, or a persisted research dossier before answering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, claims, and research objectives are sent to the remote Chukonu MCP service after OAuth authentication. <br>
Mitigation: Use the skill only where that remote service is approved for the data involved, and avoid putting secrets or private data into research prompts. <br>
Risk: Current search and research results can be incomplete, stale, or affected by retrieval gaps. <br>
Mitigation: Review failures, retrieval assessments, coverage gaps, evidence quality, and citation locators before relying on conclusions. <br>
Risk: OAuth tokens are sensitive credentials handled by the MCP host. <br>
Mitigation: Do not configure static authorization headers or expose OAuth tokens in logs, answers, examples, or error messages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hhhwor/skills/chukonu-web-search) <br>
- [Publisher profile](https://clawhub.ai/user/hhhwor) <br>
- [Chukonu MCP endpoint](https://search.houdutech.cn/web/mcp/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, and evidence-backed response instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OAuth authentication to the remote Chukonu MCP service; search and research outputs should preserve evidence, retrieval assessment, and citation relationships.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; artifact frontmatter metadata version 0.3.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
