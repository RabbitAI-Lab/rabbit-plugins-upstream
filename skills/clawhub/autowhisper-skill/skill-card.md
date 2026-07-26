## Description: <br>
AutoWhisper lets an agent drive AutoWhisper's AI CMO over an HTTP API to add products, generate marketing content, manage approvals, schedule posts, and publish to connected social channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xnjiang](https://clawhub.ai/user/xnjiang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to hand a product marketing workflow to AutoWhisper's CMO: product setup, content generation, review, scheduling, publishing, and analytics follow-up. It is intended for users who have intentionally connected AutoWhisper and any social accounts they want the service to use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an AutoWhisper API token that can access product information and connected publishing workflows. <br>
Mitigation: Keep the token private, restrict credential file permissions where possible, and rotate or revoke the token if the machine or workspace is shared. <br>
Risk: The skill can publish social content to accounts the user has connected. <br>
Mitigation: Review posts before publishing unless the user intentionally enables autonomous operation. <br>


## Reference(s): <br>
- [AutoWhisper API Reference](references/api-reference.md) <br>
- [AutoWhisper CMO Playbook](references/cmo-playbook.md) <br>
- [AutoWhisper Homepage](https://autowhisper.xyz) <br>
- [ClawHub Skill Page](https://clawhub.ai/xnjiang/skills/autowhisper-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, API calls, and relayed AutoWhisper CMO responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, schedule, approve, or publish social content through AutoWhisper when the user has provided an API token and connected destinations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
