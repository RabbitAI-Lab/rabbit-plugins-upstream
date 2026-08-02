## Description: <br>
Give AI agents hiring memory for storing, recalling, and searching candidate and interview context using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiting teams and agents use this skill to remember candidate pipeline details, interview notes, and follow-up context across conversations. It is intended for workflows where BlueColumn is approved for hiring-related data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Candidate and interview details may be stored in an external persistent memory service without clear consent, retention, or minimization controls. <br>
Mitigation: Install only where BlueColumn is approved for hiring data, obtain explicit approval before saving candidate records, minimize stored personal details, and maintain a retention and deletion process. <br>
Risk: Recruiting notes can include protected-class information, policy-restricted interview notes, or data that must remain in approved systems. <br>
Mitigation: Avoid storing protected-class information, unnecessary personal details, and policy-restricted notes; route restricted data through approved systems instead. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/hiring-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends candidate or interview context to an external persistent memory service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
