## Description: <br>
Replicate (replicate.com). Use this skill for ANY Replicate request - reading, creating, and updating data. Whenever a task involves Replicate, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent manage Replicate account, model, collection, and prediction workflows through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Creating or canceling Replicate predictions can change account state or incur cost. <br>
Mitigation: Confirm the exact payload, target prediction, and expected effect with the user before running write actions. <br>
Risk: Connector action contracts may change over time. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing each action payload. <br>
Risk: First-time setup requires installing or authenticating the oo CLI and connecting a Replicate account. <br>
Mitigation: Run setup steps only after a matching auth, connection, or missing-CLI error and only when the user trusts OOMOL and needs the connector. <br>


## Reference(s): <br>
- [Replicate homepage](https://replicate.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-replicate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run oo CLI connector actions that return JSON data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
