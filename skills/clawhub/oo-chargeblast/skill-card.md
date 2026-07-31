## Description: <br>
Chargeblast helps agents read, create, and update Chargeblast data through the OOMOL chargeblast connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Chargeblast schemas, read alerts, orders, merchants, deflection logs, and order lists, and perform approved write actions such as credit requests or alert updates through a connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Chargeblast business or payment-dispute data. <br>
Mitigation: Require the user to confirm the exact payload and expected effect before running actions tagged [write]. <br>
Risk: Incorrect action payloads can send unintended fields or values to the connector. <br>
Mitigation: Fetch the live action schema with oo connector schema before constructing each payload. <br>
Risk: The agent may access data from the user's connected Chargeblast account. <br>
Mitigation: Install and use the skill only when that account access is intended, and review requested reads and writes before execution. <br>


## Reference(s): <br>
- [Chargeblast homepage](https://www.chargeblast.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub Chargeblast skill page](https://clawhub.ai/oomol/skills/oo-chargeblast) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; connector responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
