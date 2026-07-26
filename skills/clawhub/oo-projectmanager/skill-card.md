## Description: <br>
ProjectManager helps agents search and read ProjectManager projects and tasks through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need to retrieve ProjectManager project or task information from a connected account, including project lookups and OData-filtered project or task lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad ProjectManager trigger may invoke the skill for prompts where the user intended only general discussion. <br>
Mitigation: Use the skill when ProjectManager data retrieval or workflow help is intended, and confirm intent before running external actions. <br>
Risk: The skill runs external oo CLI connector commands against a connected ProjectManager account. <br>
Mitigation: Inspect the live connector schema before constructing payloads and review external actions before allowing them. <br>


## Reference(s): <br>
- [ClawHub ProjectManager skill](https://clawhub.ai/oomol/skills/oo-projectmanager) <br>
- [ProjectManager homepage](https://www.projectmanager.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the oo CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only ProjectManager actions retrieve project and task data; connector responses include data and an execution id when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
