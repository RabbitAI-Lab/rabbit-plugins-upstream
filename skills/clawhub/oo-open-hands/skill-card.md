## Description: <br>
OpenHands (all-hands.dev). Use this skill for reading, creating, and updating OpenHands data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect OpenHands Cloud conversations, start repository tasks, check task status, and send follow-up messages through the OOMOL `oo` CLI. It is intended for agents that need schema-guided OpenHands connector actions without directly handling raw service credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can start conversations or send messages that change OpenHands state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged [write]. <br>
Risk: First-time setup may require installing or authenticating the oo CLI. <br>
Mitigation: Run setup steps only after an auth, connection, or command-not-found failure, and inspect installer and authentication steps before proceeding. <br>
Risk: Connector payloads may be invalid if action schemas change. <br>
Mitigation: Fetch the live action schema with `oo connector schema` before constructing each JSON payload. <br>


## Reference(s): <br>
- [OpenHands homepage](https://www.all-hands.dev) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-open-hands) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run with --json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
