## Description: <br>
Helps agents discover, present, and optionally install agent skills when users ask for capabilities that may already exist as installable skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to find installable skills for a requested domain or task, compare options, and receive install commands or next-step guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents toward installing additional skills, including a documented auto-confirming global install command. <br>
Mitigation: Review the exact repository and skill before installation, require explicit user approval for each install, and avoid auto-confirmed global installs. <br>
Risk: Search results or install recommendations may not match the user's needs or current package state. <br>
Mitigation: Review candidate skill pages and source files before installation, and prefer presenting options before running install commands. <br>


## Reference(s): <br>
- [ClawHub Find Skill release page](https://clawhub.ai/xiiang0529/skills/find-skill) <br>
- [Skills CLI catalog](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations and install commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
