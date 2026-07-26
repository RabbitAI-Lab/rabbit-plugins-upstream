## Description: <br>
Helps agent users and skill authors create practical Gog-style Google Workspace workflows, checklists, analyses, or code support for bugs, setup hardening, reliability improvements, and adjacent skill ideas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, skill authors, maintainers, and teams use this skill to turn Gog-style Google Workspace productivity needs into practical workflows, checklists, implementation support, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may route general Google, Workspace, Gmail, Calendar, Drive, or CLI requests to this skill. <br>
Mitigation: Review the routing behavior before installation and invoke the skill explicitly when broad activation is not desired. <br>
Risk: The skill can produce advice for account, workspace, repository, or command-line changes, but its artifacts are advisory. <br>
Mitigation: Review generated steps and require user approval before applying real account, workspace, repository, or CLI changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-110318) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Gog demand signal](https://clawhub.ai/skills/gog) <br>
- [Google Workspace demand signal](https://news.ycombinator.com/item?id=48969253) <br>
- [Agent workflow issue signal](https://github.com/yazhi-lem/open-sangam/issues/37) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, checklists, workflow plans, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory outputs; user review is required before applying account, workspace, or repository changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
