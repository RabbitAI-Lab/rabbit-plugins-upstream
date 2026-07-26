## Description: <br>
Uses the Chukonu remote MCP service to search web, academic, and patent sources, run deeper research tasks, and answer with structured evidence, retrieval assessments, and research dossiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hhhwor](https://clawhub.ai/user/hhhwor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research-oriented agents use this skill to run current web, academic, and patent searches through a remote MCP service, then escalate to persistent research when the task needs fact checking, counterevidence, PDF review, or coverage assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, research objectives, and related context are sent to the Chukonu MCP service. <br>
Mitigation: Avoid using the skill for confidential research unless the provider's privacy terms meet the user's needs. <br>
Risk: OAuth credentials are stored and managed by the MCP host. <br>
Mitigation: Use the host's OAuth flow, do not configure static Authorization headers, and avoid exposing tokens in logs, examples, or answers. <br>
Risk: Search rankings and completed research runs can be mistaken for factual certainty. <br>
Mitigation: Base conclusions on cited evidence, retrieval assessments, coverage gaps, and dossier assessments rather than relevance scores or task completion state alone. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hhhwor/skills/chukonu-web-search) <br>
- [Chukonu Web Search MCP Endpoint](https://search.houdutech.cn/web/mcp/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Evidence-grounded responses should preserve links between findings, evidence IDs, and source locators.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
