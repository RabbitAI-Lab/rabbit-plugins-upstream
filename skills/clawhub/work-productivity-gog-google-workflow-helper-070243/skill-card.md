## Description: <br>
Helps agent users and skill authors plan, harden, debug, and adapt Gog-style Google Workspace workflows into practical, local-friendly guides, checklists, and implementation support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace workflow needs into actionable plans, checklists, bug-fix guidance, reliability improvements, and adjacent workflow designs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked by broad Google, workflow, CLI, or productivity triggers when a user intended a narrower helper. <br>
Mitigation: Review trigger behavior before deployment and narrow or disable implicit invocation when accidental activation would disrupt the workspace. <br>
Risk: The skill produces advisory plans and workflow guidance that could affect Gmail, Calendar, Drive, Contacts, or business data if applied without review. <br>
Mitigation: Treat outputs as proposals, confirm assumptions and permissions, and test changes on non-critical data before using them in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-070243) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [New mandatory Gmail, your Android backup storage needs may increase](https://news.ycombinator.com/item?id=48969253) <br>
- [Open source Termany: Agent-Native terminal](https://www.v2ex.com/t/1228797) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory output; users should verify proposed workflows before applying them to real Google Workspace or business data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
