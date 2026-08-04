## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create Tavily-style web-search workflows, checklists, analyses, code changes, and reliability improvements grounded in documented demand signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn Tavily-style web-search workflow demand into practical plans, checklists, implementation support, and verification notes. It is intended for reliability, safety hardening, bug-fixing, and adjacent workflow design around web-search agent tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording and implicit invocation could cause the skill to activate for general web-search or Tavily-adjacent requests where it is not needed. <br>
Mitigation: Narrow or disable implicit invocation so the skill activates only for explicit Tavily or web-search workflow requests. <br>
Risk: Generated workflow, code, configuration, or shell-command guidance could be incorrect or unsuitable for a user's environment. <br>
Mitigation: Review proposed outputs, scan any generated artifacts, and validate results against the stated success criteria before deployment or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-235619) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: Multi Search Engine](https://clawhub.ai/skills/multi-search-engine) <br>
- [Popular ClawHub skill demand: Weather](https://clawhub.ai/skills/weather) <br>
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Popular ClawHub skill demand: Obsidian](https://clawhub.ai/skills/obsidian) <br>
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix) <br>
- [Popular ClawHub skill demand: Tavily Search](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Popular ClawHub skill demand: PollyReach](https://clawhub.ai/skills/pollyreach) <br>
- [Hacker News Ask HN signal: ChatBOT chapter thread](https://news.ycombinator.com/item?id=48989672) <br>
- [Hacker News Ask HN signal: GitHub GraphQL API returns missing data](https://news.ycombinator.com/item?id=49003232) <br>
- [V2EX latest signal: remote work roles](https://www.v2ex.com/t/1229141) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored workflow steps, reusable checklists, implementation notes, assumptions, limits, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
