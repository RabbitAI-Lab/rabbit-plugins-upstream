## Description: <br>
Sender lets an agent read and manage Sender campaigns, subscribers, groups, custom fields, and workflows through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use Sender to inspect live connector schemas and then read or modify Sender account data such as subscribers, groups, campaigns, fields, and workflows through approved oo CLI actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or update subscribers, fields, or group memberships in the connected Sender account. <br>
Mitigation: Require the agent to show the exact payload and expected effect before approving any write action. <br>
Risk: The destructive group removal action can remove subscribers from Sender groups. <br>
Mitigation: Confirm the target subscribers, selection criteria, and group before running destructive actions. <br>


## Reference(s): <br>
- [Sender homepage](https://www.sender.net) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sender) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the oo CLI; connector responses are JSON with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
