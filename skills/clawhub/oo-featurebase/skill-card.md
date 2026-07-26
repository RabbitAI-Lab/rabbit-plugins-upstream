## Description: <br>
Featurebase (featurebase.app). Use this skill for ANY Featurebase request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage Featurebase boards, contacts, and feedback posts through an OOMOL-connected Featurebase account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create, update, upsert, and delete actions can change live Featurebase data. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write or destructive actions. <br>
Risk: Deleting contacts or posts removes live Featurebase records. <br>
Mitigation: Require explicit approval for the target contact or post before running destructive actions. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing each payload. <br>


## Reference(s): <br>
- [Featurebase homepage](https://www.featurebase.app/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-featurebase) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Featurebase action results as JSON when run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
