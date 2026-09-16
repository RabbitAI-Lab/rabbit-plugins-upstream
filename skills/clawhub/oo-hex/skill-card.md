## Description:

Operate Hex through an OOMOL-connected account to list projects and runs, inspect project or run details, trigger published project runs, and cancel in-progress runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Hex projects from an agent through the OOMOL oo CLI, including reading project metadata, monitoring runs, and triggering or cancelling runs with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands.

Mitigation: Use a verified installation path where possible, and do not allow an agent to run the remote installer automatically.

Risk: Triggering or cancelling Hex runs changes state in the connected Hex account.

Mitigation: Require explicit user confirmation of the exact payload and effect before running state-changing actions.

Risk: Connector access depends on the connected OOMOL and Hex account scope.

Mitigation: Install only when OOMOL and the connected Hex account scope are trusted and appropriate for the intended use.

## Reference(s):

- [Hex homepage](https://hex.tech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Hex skill](https://clawhub.ai/oomol/skills/oo-hex)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector calls can return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: evidence release version and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
