## Description: <br>
ShipBob (shipbob.com) skill for searching and reading ShipBob data through the OOMOL ship_bob connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to query connected ShipBob accounts for inventory, channel, fulfillment location, and product catalog information through the OOMOL oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the OOMOL oo CLI to query data from a connected ShipBob account. <br>
Mitigation: Install and use it only when comfortable with OOMOL account access, and review OOMOL setup and ShipBob connection steps before use. <br>
Risk: Future connector actions could include write or destructive operations even though the current listed actions are reads. <br>
Mitigation: Do not approve write or destructive actions unless the exact ShipBob payload, target, and expected effect are clear. <br>


## Reference(s): <br>
- [ClawHub ShipBob skill page](https://clawhub.ai/oomol/skills/oo-ship-bob) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ShipBob homepage](https://www.shipbob.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include proposed oo CLI schema and connector run commands; connector responses are JSON objects with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
