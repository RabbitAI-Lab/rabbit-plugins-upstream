## Description: <br>
Helps agent users, skill authors, maintainers, and teams produce practical workflows, artifacts, checklists, analysis, code changes, or decision support for GitHub-style software tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, skill authors, and agent users use this skill to structure GitHub-style software work such as bug fixes, setup hardening, reliability improvements, issue or PR workflows, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and implicit invocation may activate the skill for unrelated software, GitHub, CLI, issue, API, or bug-fix requests. <br>
Mitigation: Prefer explicit invocation when possible and confirm that the requested task matches the skill before relying on its workflow. <br>
Risk: Generated repository, issue, PR, or command-line recommendations may be incorrect or unsafe for the target project. <br>
Mitigation: Review proposed actions before execution or application, and run the relevant project tests, scans, or verification commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-130446) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Ask HN: Due to spam on GitHub, what platforms can I move my projects?](https://news.ycombinator.com/item?id=48611303) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Popular ClawHub skill demand: Weather](https://clawhub.ai/skills/weather) <br>
- [Popular ClawHub skill demand: Obsidian](https://clawhub.ai/skills/obsidian) <br>
- [Popular ClawHub skill demand: Nano Pdf](https://clawhub.ai/skills/nano-pdf) <br>
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix) <br>
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [GitHub Banned All CI for Our OSS Org Because of Bad Drive-By Contributors](https://news.ycombinator.com/item?id=48624574) <br>
- [Exercise: Integrate MCP with Copilot](https://github.com/420KanaCoin/integrate-mcp-with-copilot/issues/1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, verification steps, and remaining risks when applicable.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
