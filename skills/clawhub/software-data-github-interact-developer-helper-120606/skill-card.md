## Description: <br>
Helps agent users, skill authors, maintainers, and teams create GitHub-style workflows for bug fixing, setup hardening, reliability improvements, and adjacent ClawHub skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent users, skill authors, and maintainers use this skill to turn GitHub-style development needs into practical workflows, checklists, code changes, analyses, and verification notes. It is suited for bug fixes, CLI and issue workflows, setup hardening, reliability improvements, and related skill-authoring support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad routing language may activate the skill for general GitHub, CLI, API, issue, or bug-fix requests. <br>
Mitigation: Use it when the user explicitly wants repository or developer-workflow help, and narrow triggers before deployment when a stricter routing boundary is required. <br>
Risk: The skill may provide implementation guidance or code changes that need project-specific validation. <br>
Mitigation: Review proposed changes and run the included verification or test commands before applying them to a live workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-120606) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: Weather](https://clawhub.ai/skills/weather) <br>
- [Ask HN: Active GitHub accounts probably delivering malware](https://news.ycombinator.com/item?id=48548530) <br>
- [Ask HN: AI dev in the cloud](https://news.ycombinator.com/item?id=48543969) <br>
- [Ask HN: Claude renamed my VM from the inside](https://news.ycombinator.com/item?id=48551386) <br>
- [Ask HN: Spec-kit specs](https://news.ycombinator.com/item?id=48539057) <br>
- [V2EX: Small model training platform](https://www.v2ex.com/t/1220893) <br>
- [V2EX: Kiwi v1.0.0 release](https://www.v2ex.com/t/1220865) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and concise verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable workflows, checklists, implementation steps, assumptions, limits, and follow-up risks.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
