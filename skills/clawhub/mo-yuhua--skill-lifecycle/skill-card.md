## Description: <br>
Skill Lifecycle standardizes skill development, testing, quality scanning, Git commits, and optional ClawHub publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mo-yuhua](https://clawhub.ai/user/mo-yuhua) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to automate routine lifecycle tasks for ClawHub skills, including version updates, tests, quality scans, Git commits, batch processing, and optional publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify skill files and metadata during version, configuration, development, and batch workflows. <br>
Mitigation: Run it only inside repositories intended for modification, and use dry-run or check modes before applying changes. <br>
Risk: The development flow can create Git commits after detecting repository changes. <br>
Mitigation: Review Git status and the proposed commit message before allowing automated commit steps. <br>
Risk: The optional publishing flow relies on the local ClawHub CLI session and can publish the current skill version. <br>
Mitigation: Confirm the active ClawHub account and run publishing prerequisite checks before publishing. <br>


## Reference(s): <br>
- [Skill Lifecycle on ClawHub](https://clawhub.ai/mo-yuhua/skill-lifecycle) <br>
- [Publisher profile: mo-yuhua](https://clawhub.ai/user/mo-yuhua) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Text, Guidance] <br>
**Output Format:** [Terminal output, Markdown guidance, YAML or JSON configuration, and repository file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update skill metadata, configuration files, Git state, and optional ClawHub publish records when run in non-dry-run modes.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
