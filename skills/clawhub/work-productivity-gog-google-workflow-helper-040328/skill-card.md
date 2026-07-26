## Description: <br>
Helps agent users and skill authors turn Gog-style Google Workspace workflow requests into practical plans, checklists, templates, code changes, and validation notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, skill authors, maintainers, and teams use this skill to convert Gog-style Google Workspace or productivity requests into repeatable workflows, artifacts, checklists, implementation support, or decision aids. It is aimed at local-hardware-friendly guidance that clarifies success criteria and validates the delivered result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may route general Google, CLI, or productivity requests to this skill when a narrower skill would be more appropriate. <br>
Mitigation: Use explicit task context and success criteria before applying the workflow, and narrow invocation triggers in downstream packaging when possible. <br>
Risk: Workflow or code-change guidance can be incomplete or mismatched to a user's actual Google Workspace environment. <br>
Mitigation: Ask only for materially missing inputs, state assumptions, and validate outputs against the user's stated success criteria before finalizing. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-040328) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: self-improving agent](https://clawhub.ai/skills/self-improving-agent) <br>
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Popular ClawHub skill demand: Obsidian](https://clawhub.ai/skills/obsidian) <br>
- [Popular ClawHub skill demand: Nano Pdf](https://clawhub.ai/skills/nano-pdf) <br>
- [Popular ClawHub skill demand: PollyReach](https://clawhub.ai/skills/pollyreach) <br>
- [Hacker News demand signal: Is GPT-5.6 Sol Max Worth It?](https://news.ycombinator.com/item?id=48947713) <br>
- [Hacker News demand signal: Where is your GitHub network building from?](https://news.ycombinator.com/item?id=48945115) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code, shell command, checklist, or template blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
