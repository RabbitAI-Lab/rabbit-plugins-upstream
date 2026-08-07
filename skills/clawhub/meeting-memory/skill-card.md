## Description: <br>
Gives agents a BlueColumn-backed meeting memory for storing, recalling, and searching meeting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent store meeting notes in BlueColumn, recall prior action items, and search meeting context during later interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting notes and recall queries may be sent to and persisted in an external BlueColumn service without clear consent, retention, or sensitivity guidance. <br>
Mitigation: Confirm approved data categories, access controls, retention, deletion procedures, and user consent before use; avoid secrets, regulated data, and confidential meetings unless the organization has approved that use. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/meeting-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends meeting content to BlueColumn for persistent storage.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
