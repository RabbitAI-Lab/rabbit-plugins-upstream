## Description: <br>
Novu (novu.co) helps agents read, create, and update Novu data through the OOMOL connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Novu through an OOMOL-connected account, including subscriber lookup, subscriber changes, and workflow event triggering through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, and trigger-event actions can change Novu subscribers or send workflow events. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running any write action. <br>
Risk: Running setup commands unnecessarily can install software or start authentication flows the user did not need. <br>
Mitigation: Run setup only after a matching command failure, such as a missing oo CLI, authentication error, expired credential, or missing Novu connection. <br>
Risk: Payloads built without the live connector schema can be malformed or affect the wrong target. <br>
Mitigation: Inspect the action schema with the oo CLI before constructing the JSON payload for an action. <br>


## Reference(s): <br>
- [ClawHub Novu Skill](https://clawhub.ai/oomol/skills/oo-novu) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Novu Homepage](https://novu.co) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; state-changing actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
