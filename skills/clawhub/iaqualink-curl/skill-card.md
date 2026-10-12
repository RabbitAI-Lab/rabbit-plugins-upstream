## Description:

Helps users query iAqualink pool systems from a shell with curl for device status, temperatures, auxiliary circuits, and chlorinator state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and pool-system owners use this skill for one-off equipment-status checks, shell scripting, and iAqualink API debugging without running an MCP server. Its command helper also permits equipment changes, for which a confirmed-control tool is preferable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sourcing the helper reads an iAqualink credential from Keychain, stores session tokens locally, and calls the iAqualink cloud.

Mitigation: Review the helper before sourcing it, use it only in trusted shells and scripts, and protect or delete the local session file when finished.

Risk: The raw command helper and documented write examples can change pool equipment; toggle commands can reverse the intended state.

Mitigation: Prefer a confirmed-control tool for changes; read the current state first and send a toggle only when the state differs.

## Reference(s):

- [ClawHub iaqualink-curl release](https://clawhub.ai/chrischall/skills/iaqualink-curl)
- [iAqualink shell helper](references/iaqualink.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The shell helper returns iAqualink JSON responses; live verification of most endpoints is pending.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
