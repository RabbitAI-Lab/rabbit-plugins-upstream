## Description:

DACHSER helps agents operate DACHSER through an OOMOL-connected account for reading, creating, and updating DACHSER data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to inspect DACHSER action schemas, run DACHSER connector actions with JSON payloads, retrieve shipment status and history, and check delivery-order status through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the oo CLI installation path, prefer a signed or package-manager installation, or download and verify the installer before execution.

Risk: Write-tagged or destructive actions may change DACHSER state, and one listed retrieval action is tagged as write.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write-tagged or destructive actions.

## Reference(s):

- [ClawHub DACHSER Skill](https://clawhub.ai/oomol/skills/oo-dachser)
- [DACHSER Homepage](https://www.dachser.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo CLI connector schemas before action execution; command responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
