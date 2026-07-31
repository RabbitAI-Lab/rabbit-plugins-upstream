## Description: <br>
Dart lets an agent read, create, update, and delete Dart tasks through OOMOL's oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent manage Dart workspace tasks through an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing Dart actions can create, update, or delete tasks. <br>
Mitigation: Confirm the exact payload and intended effect before write actions, and require explicit user approval before deleting a task. <br>
Risk: Connector input contracts may change over time. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing a payload. <br>
Risk: First-time setup can install an external command-line tool through a remote installer. <br>
Mitigation: Apply normal external CLI installation trust review before running the installer. <br>


## Reference(s): <br>
- [ClawHub Dart skill page](https://clawhub.ai/oomol/skills/oo-dart) <br>
- [Dart homepage](https://www.dartai.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live schema inspection with oo connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
