## Description: <br>
Helps agent users and skill authors plan, build, validate, and harden Tavily-style web search productivity workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Tavily-style web search workflow requests into practical plans, checklists, implementation support, and verification notes for reliable local-friendly agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate too broadly for ordinary web, search, API, or help requests. <br>
Mitigation: Invoke it explicitly for Tavily or web-search workflow tasks, and narrow or disable implicit invocation where precise routing is required. <br>
Risk: Generated plans, commands, or code changes may be incomplete or unsuitable for a user's environment. <br>
Mitigation: Review proposed artifacts before use and validate them against the stated success criteria and local constraints. <br>


## Reference(s): <br>
- [Published ClawHub Skill](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-234020) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Tavily Search Demand Signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Vector Search Demand Signal](https://news.ycombinator.com/item?id=48939470) <br>
- [Source Library Issue Demand Signal](https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/issues/3170) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, limits, remaining risks, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
