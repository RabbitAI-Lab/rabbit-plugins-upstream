## Description: <br>
Track water and sleep with JSON file storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stellarhold170nt](https://clawhub.ai/user/stellarhold170nt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to record water intake, sleep and wake events, view simple daily statistics, and update or delete recent water entries in a local JSON file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs local Node.js one-liners that write water and sleep history to {baseDir}/health-data.json. <br>
Mitigation: Review commands before execution and keep backups if records need to be recoverable. <br>
Risk: Cup values inserted into command examples may be invalid if not checked before execution. <br>
Mitigation: Validate cup values as numbers before substituting them into the command. <br>
Risk: Update and delete actions can overwrite or remove the most recent water record. <br>
Mitigation: Confirm the target record and maintain backups when preserving history matters. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, JSON] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON file records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Node.js built-in modules to read and write local health tracking records in {baseDir}/health-data.json.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
