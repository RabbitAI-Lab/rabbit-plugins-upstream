## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn SkillScan-style security and reliability needs into practical workflows, checklists, analyses, code changes, and decision support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to clarify security and reliability goals, produce practical SkillScan-style workflows or artifacts, and validate outputs against visible success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit activation may select the skill for ordinary productivity or security prompts where a narrower helper would be more appropriate. <br>
Mitigation: Review activation settings before installation and prefer explicit invocation or narrower trigger terms for deployments that need predictable routing. <br>
Risk: The skill can produce workflow, checklist, code, shell-command, or configuration guidance that may be unsuitable for a specific environment. <br>
Mitigation: Review generated artifacts against local requirements and scan or test any proposed code, commands, or configuration before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Release Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-030357) <br>
- [ClawHub SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>
- [ClawHub Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [ClawHub Self-Improving Agent Demand Signal](https://clawhub.ai/skills/self-improving-agent) <br>
- [OpenAI Codex Issue Demand Signal](https://github.com/openai/codex/issues/34668) <br>
- [Agent CLIs Diagrams Issue Demand Signal](https://github.com/agent-clis/diagrams/issues/25) <br>
- [Hacker News AI Workflow Demand Signal](https://news.ycombinator.com/item?id=48979474) <br>
- [Hacker News 2FA Security Demand Signal](https://news.ycombinator.com/item?id=48976781) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
