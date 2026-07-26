## Description: <br>
LogSnag helps agents operate LogSnag through an OOMOL-connected account using the oo CLI for events, insights, and user profile updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams managing LogSnag use this skill to publish project events and insight values, update user profiles, and mutate numeric insights through schema-checked oo CLI actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Some state-changing LogSnag actions may not be clearly labeled as requiring confirmation. <br>
Mitigation: Require explicit user confirmation for identify_user, mutate_insight, publish_event, and publish_insight after reviewing the exact payload and expected effect. <br>
Risk: First-time setup may install or authenticate the oo CLI before the user actually needs it. <br>
Mitigation: Only run first-time setup after an auth, connection, or missing-command failure, and verify the oo CLI installer before use. <br>


## Reference(s): <br>
- [LogSnag homepage](https://logsnag.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub LogSnag skill page](https://clawhub.ai/oomol/skills/oo-logsnag) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId; state-changing actions should be confirmed with the user before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
