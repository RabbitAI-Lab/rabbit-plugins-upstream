## Description: <br>
Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robin797860](https://clawhub.ai/user/robin797860) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to search for installable skills, present relevant options, and offer installation commands when a task may be better handled by a specialized skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer broad help requests toward installing third-party skills globally and may skip confirmation prompts. <br>
Mitigation: Review the package source and publisher before installation, avoid auto-confirm installs unless trusted, and prefer scoped or reversible installs where available. <br>
Risk: Search results and suggested skills may not match the user's actual task or risk tolerance. <br>
Mitigation: Present the skill purpose, publisher, install command, and reference link for user review before proceeding with installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robin797860/skills/find-skills-robin) <br>
- [Skills ecosystem browser](https://skills.sh/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend or run Skills CLI searches and propose skill installation commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
