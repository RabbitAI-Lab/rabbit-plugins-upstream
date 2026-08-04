## Description: <br>
Give AI agents persistent BlueColumn research memory for storing, recalling, and searching research context, requiring a BlueColumn API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to give an agent persistent research memory through BlueColumn, including storing research notes, creating quick notes, and recalling prior findings during later interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead agents to store conversation summaries in a third-party persistent memory service. <br>
Mitigation: Use it only for research notes intentionally approved for BlueColumn storage, and avoid secrets, credentials, personal data, confidential business information, and regulated content unless an explicit storage policy allows it. <br>
Risk: The artifact requires a BlueColumn API key and directs agents to read it from available key storage. <br>
Mitigation: Confirm key handling policy before installation and limit access to the BlueColumn API key to agents and workflows that need persistent research memory. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/research-memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and API usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for agent memory API calls; does not itself store data without an agent executing the described requests.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
