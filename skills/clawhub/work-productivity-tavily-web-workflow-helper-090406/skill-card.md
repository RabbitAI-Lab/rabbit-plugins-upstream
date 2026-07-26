## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn Tavily-search-style productivity needs into practical workflows, checklists, analysis, code changes, and validation notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External AI-agent users, skill authors, maintainers, and teams use this skill to convert search and web workflow needs into concrete implementation plans, reusable checklists, automation outlines, analysis, code edits, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for broad web, search, API, or productivity prompts beyond the intended Tavily-style workflow helper scope. <br>
Mitigation: Confirm the user request matches a search or web workflow productivity need before applying the skill, and tighten trigger wording during review if accidental invocation is observed. <br>
Risk: Advisory workflow, code, configuration, or shell-command suggestions can be incomplete or incorrect for the user's environment. <br>
Mitigation: Review generated changes before use, run local validation where applicable, and preserve the skill's requirement to list assumptions, limits, and remaining risks. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Release Page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-090406) <br>
- [OpenClaw Tavily Search Demand Signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [GitHub Issue Demand Signal](https://github.com/legend-esc/carbonchain/issues/508) <br>
- [Hacker News Demand Signal](https://news.ycombinator.com/item?id=49003232) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with checklists, plans, prose, and code or shell snippets when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, limits, validation notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
