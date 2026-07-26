## Description: <br>
Manage Trello boards, lists, and cards via the Trello REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaunceyliu](https://clawhub.ai/user/chaunceyliu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect Trello boards, lists, and cards and to create, move, comment on, or archive cards through Trello REST API commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trello API credentials can grant access to boards available to the token. <br>
Mitigation: Use a limited-scope token where possible, keep credentials out of shared logs, and prefer a test board for validation. <br>
Risk: Create, move, comment, and archive commands make real changes to Trello data. <br>
Mitigation: Review the command, board ID, list ID, card ID, and payload before execution. <br>
Risk: High-volume requests can hit Trello API rate limits. <br>
Mitigation: Throttle repeated requests and batch operations within Trello's documented limits. <br>


## Reference(s): <br>
- [Trello REST API documentation](https://developer.atlassian.com/cloud/trello/rest/) <br>
- [Trello API key page](https://trello.com/app-key) <br>
- [ClawHub skill page](https://clawhub.ai/chaunceyliu/skills/test1) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require jq and Trello credentials in TRELLO_API_KEY and TRELLO_TOKEN.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
