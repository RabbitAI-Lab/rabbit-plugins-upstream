## Description: <br>
Helps agents read Umami analytics through the OOMOL oo CLI, including websites, metrics, pageviews, realtime visitors, and events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and analytics teams use this skill to query Umami website analytics from an OOMOL-connected account. It supports read-oriented workflows such as listing websites, checking aggregate stats, reviewing traffic metrics, inspecting pageviews, and viewing realtime visitors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Service credentials may grant broader Umami access than the user intends. <br>
Mitigation: Configure Umami tokens with the minimum permissions needed for the intended analytics workflows. <br>
Risk: Connector action inputs may drift from the examples or from an agent's assumptions. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before constructing each payload. <br>
Risk: Authentication, connection, or billing setup commands may create unwanted account-side effects if run proactively. <br>
Mitigation: Run setup, login, connection, or billing steps only after the matching command failure or user request. <br>
Risk: Future write or destructive connector actions could change or remove Umami data. <br>
Mitigation: Confirm the exact payload, target, and effect with the user before running any action tagged `[write]` or `[destructive]`. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-umami) <br>
- [Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Umami Homepage](https://umami.is) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; results include an execution id under meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
