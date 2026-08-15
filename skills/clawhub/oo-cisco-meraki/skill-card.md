## Description:

Cisco Meraki (meraki.cisco.com). Use this skill for ANY Cisco Meraki request - searching and reading data. Whenever a task involves Cisco Meraki, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and IT or network operations teams use this skill to inspect Cisco Meraki organizations, networks, devices, and inventory through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read Cisco Meraki organization, network, and device inventory through the connected OOMOL account.

Mitigation: Install and use it only when that account-level read access is appropriate for the agent's task.

Risk: Future actions tagged write or destructive could change or remove Cisco Meraki state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action.

Risk: First-time setup may require installing the oo CLI from an external install source.

Mitigation: Review the oo CLI install source before setup in environments with strict software supply-chain controls.

## Reference(s):

- [ClawHub Cisco Meraki Skill](https://clawhub.ai/oomol/skills/oo-cisco-meraki)
- [Cisco Meraki](https://meraki.cisco.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-only Cisco Meraki queries through the oo CLI; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
