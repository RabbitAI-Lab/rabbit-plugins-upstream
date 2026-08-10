## Description: <br>
Helps agents store, recall, and search Gmail thread context using BlueColumn persistent memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent manages Gmail conversations and needs to remember thread summaries, recall prior context, or search saved email-memory notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email-thread summaries may include confidential, legal, financial, medical, or personal information. <br>
Mitigation: Review the skill before installing it for sensitive Gmail accounts and avoid storing sensitive summaries by default. <br>
Risk: The skill stores Gmail context in a third-party persistent memory service without clear consent or retention limits in the artifact. <br>
Mitigation: Confirm BlueColumn retention and deletion controls before broad use, and make storage decisions explicit to the user or administrator. <br>
Risk: The BlueColumn API key grants access to memory operations. <br>
Mitigation: Store the BlueColumn key in a managed secret store and avoid exposing it in prompts, logs, or checked-in files. <br>


## Reference(s): <br>
- [BlueColumn API documentation](https://bluecolumn.ai/docs) <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/gmail-memory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a BlueColumn API key and sends thread notes or recall queries to BlueColumn endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
