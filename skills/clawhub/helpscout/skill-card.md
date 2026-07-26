## Description: <br>
Fetch and reply to Helpscout conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fabiensebban](https://clawhub.ai/user/fabiensebban) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Support teams and developers use this skill to fetch HelpScout conversations from configured inboxes, filter ticket data, and create internal notes or replies through the HelpScout API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access support conversations and mutate tickets, while the security evidence flags inconsistent write behavior and inbox scoping. <br>
Mitigation: Review HelpScout app permissions, use least-privilege credentials, verify inbox filtering, and require human approval before any note or reply is posted. <br>
Risk: Security guidance calls out vulnerable unused dependencies as a production concern. <br>
Mitigation: Update or remove vulnerable unused dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub Helpscout Skill Page](https://clawhub.ai/fabiensebban/skills/helpscout) <br>
- [HelpScout API Documentation Reference](references/helpscout-api.md) <br>
- [HelpScout API Docs](https://developer.helpscout.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples, shell commands, configuration snippets, and API result data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HelpScout API credentials and configured inbox IDs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
