## Description:

NetSuite (netsuite.com). Use this skill for ANY NetSuite request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to inspect NetSuite action schemas and run connected-account actions for reading, creating, listing, querying, and updating NetSuite records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on sensitive NetSuite business data through create, update, and SuiteQL actions.

Mitigation: Confirm the exact payload and expected effect with the user before running any write or SuiteQL action.

Risk: First-time setup may install the oo CLI through a remote shell installer.

Mitigation: Review the official installer or use a verified package or installation method before granting CLI access.

## Reference(s):

- [ClawHub NetSuite skill page](https://clawhub.ai/oomol/skills/oo-netsuite)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [NetSuite homepage](https://www.netsuite.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
