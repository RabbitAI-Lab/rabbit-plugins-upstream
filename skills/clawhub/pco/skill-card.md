## Description: <br>
Provides command-line guidance for using a PCO CLI to manage Planning Center Services resources through the Planning Center Services API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubyrunsstuff](https://clawhub.ai/user/rubyrunsstuff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Church operations staff and developers use this skill to plan or run PCO CLI commands for Planning Center Services data such as plans, service types, teams, songs, media, scheduled people, and raw API requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill points to unbundled local CLI code and dependencies. <br>
Mitigation: Install or use it only after separately reviewing the external pco.ts CLI and its dependencies. <br>
Risk: Raw API commands can change or delete live Planning Center data. <br>
Mitigation: Use least-privilege Planning Center credentials and require explicit human confirmation before any raw POST, PATCH, or DELETE command. <br>
Risk: Command outputs may include people or scheduling data. <br>
Mitigation: Avoid sharing outputs that contain personal, team, or scheduling information outside authorized church operations workflows. <br>


## Reference(s): <br>
- [Planning Center Services API documentation](https://developer.planning.center/docs/#/apps/services) <br>
- [ClawHub skill page](https://clawhub.ai/rubyrunsstuff/skills/pco) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that query or mutate Planning Center Services data; raw POST, PATCH, and DELETE requests require human confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
