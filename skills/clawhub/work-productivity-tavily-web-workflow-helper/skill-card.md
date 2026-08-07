## Description: <br>
Helps AI-agent users and skill authors create Tavily-style web workflow plans, checklists, analysis, code changes, and decision support for bug fixing, setup hardening, reliability improvement, or adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn demand for Tavily-style web search workflows into practical local-friendly plans, templates, checklists, implementation support, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be selected too broadly because implicit invocation is enabled and trigger words are generic. <br>
Mitigation: Invoke it by name for Tavily-style workflow work and scope requests to concrete web search workflow, setup, reliability, or adjacent skill tasks. <br>
Risk: Workflow advice, code changes, or configuration suggestions may be incorrect or too general for the user's environment. <br>
Mitigation: Review generated artifacts, confirm assumptions and constraints, and run local validation before deployment or reuse. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper) <br>
- [Tavily Search Demand Signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Multi Search Engine Demand Signal](https://clawhub.ai/skills/multi-search-engine) <br>
- [Agent Browser Demand Signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Reliability and Worst-Case Latency Signal](https://github.com/zig-utils/zig-js/issues/493) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, configuration snippets, checklists, and validation notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompt-only workflow helper; no bundled executable code or credential handling is included.] <br>

## Skill Version(s): <br>
0.20260802.40421 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
