## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Tavily-style web search workflows, bug-fix plans, setup hardening checklists, reliability improvements, and adjacent skill designs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn Tavily-style web search and work-productivity needs into actionable workflows, checklists, analyses, code changes, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger keywords and implicit invocation may activate the skill for unrelated web, search, API, or productivity prompts. <br>
Mitigation: Narrow or disable implicit invocation when installing the skill, and review whether the Tavily/web-search workflow context matches the current task before using its guidance. <br>
Risk: Workflow proposals may be incomplete or unsuitable for a user's specific setup because the skill produces documentation and guidance rather than executing verified integrations. <br>
Mitigation: Review generated plans, checklists, commands, and configuration snippets against local requirements before applying them. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-100358) <br>
- [Popular ClawHub skill demand: Tavily Search](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Ask HN: Claude Code for Ordinary User](https://news.ycombinator.com/item?id=48955119) <br>
- [V2EX: Daily Hot API with AI Market Analysis](https://www.v2ex.com/t/1228342) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code blocks, shell commands, configuration snippets, checklists, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's immediate context and should make assumptions, limits, required inputs, and follow-up risks visible.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
