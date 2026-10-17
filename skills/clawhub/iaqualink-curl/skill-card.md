## Description:

Provides shell recipes for signing in to iAqualink, listing pool systems, and reading iAqua status or an eXO chlorinator shadow without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Pool owners and developers can check iAqualink temperatures and equipment status from a terminal or script, and troubleshoot cloud API reads. Equipment control is available but should be handled cautiously.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shell helper accesses iAqualink credentials and the vendor cloud account.

Mitigation: Install only if comfortable granting this access; protect the local session file and use reads by default.

Risk: Write commands can change physical pool equipment, and toggle commands may switch pumps, heaters, or auxiliaries the wrong way.

Mitigation: Avoid writes unless intended; manually check the current state first and prefer controls that verify changes.

## Reference(s):

- [iAqualink shell helper](references/iaqualink.sh)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/iaqualink-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands return JSON pool status; the eXO shadow read has not been verified live.]

## Skill Version(s):

0.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
