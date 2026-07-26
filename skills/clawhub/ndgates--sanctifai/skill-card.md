## Description: <br>
Interface with the SanctifAI Human-in-the-Loop API to create tasks and wait for human responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ndgates](https://clawhub.ai/user/ndgates) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agent builders use this skill to delegate approvals, reviews, data entry, fact verification, and other structured decisions to human reviewers through SanctifAI MCP or REST workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tasks, prompts, and attachments may expose sensitive, regulated, or confidential information to SanctifAI and external human reviewers. <br>
Mitigation: Share only information the user is authorized to disclose, avoid secrets and regulated personal data, and prefer guild or direct routing for trusted reviewers when appropriate. <br>
Risk: API keys, webhook secrets, callback URLs, and invite links can grant access or reveal task activity if mishandled. <br>
Mitigation: Protect SanctifAI credentials like account secrets, verify invite recipients and callback URLs, rotate keys when needed, and validate webhook signatures. <br>
Risk: Paid tasks can spend organization wallet funds or trigger funding workflows. <br>
Mitigation: Confirm task pricing, wallet funding, and spending limits before creating paid tasks. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ndgates/skills/sanctifai) <br>
- [SanctifAI API Quick Start](https://app.sanctifai.com/v1) <br>
- [SanctifAI OpenAPI Specification](https://app.sanctifai.com/v1/openapi.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documentation with HTTP, JSON, Python, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents through external MCP and REST API calls; completed task responses are returned as structured JSON by the SanctifAI service.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
