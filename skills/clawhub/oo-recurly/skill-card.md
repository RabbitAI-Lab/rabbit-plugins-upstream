## Description: <br>
Recurly lets an agent read, create, and update Recurly accounts, plans, and subscriptions through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to inspect and manage Recurly billing objects through the OOMOL oo CLI without handling raw Recurly credentials directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may expose customer, account, subscription, and billing data. <br>
Mitigation: Install and use the skill only when the agent is expected to access Recurly, and treat returned billing data as sensitive. <br>
Risk: Write actions can change billing-related data such as accounts, plans, and subscriptions. <br>
Mitigation: Review every write payload and confirm the intended effect with the user before approving changes. <br>
Risk: Action payloads may become incorrect if the connector contract changes. <br>
Mitigation: Inspect the live action schema before building or running each connector payload. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-recurly) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Recurly Homepage](https://recurly.com) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [OOMOL Recurly Connection](https://console.oomol.com/app-connections?provider=recurly) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before running Recurly actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
