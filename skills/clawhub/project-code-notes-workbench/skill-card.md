## Description:

Builds a delivery ledger entry from project context and appends it to a local ledger.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Project delivery and operations teams use this skill to turn prepared project context into a delivery entry and record it in a local ledger.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project details in the input may be retained in a local ledger file.

Mitigation: Choose a dedicated output directory and avoid sensitive project context unless local JSONL storage is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/project-code-notes-workbench)
- [Usage and execution guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and local JSONL ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a delivery entry and a receipt for the locally appended record.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
