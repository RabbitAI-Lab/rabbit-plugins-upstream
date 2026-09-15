## Description:

Kernel helps an agent manage Kernel browser sessions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to create, inspect, list, update, and delete Kernel browser sessions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill setup references running an internet installer directly in a shell, which evidence.security flags as suspicious.

Mitigation: Install only from a trusted OOMOL CLI distribution path; prefer versioned downloads and verify checksum or signature before running installer commands.

Risk: The skill can create, update, and delete Kernel browser sessions through a connected account.

Mitigation: Confirm exact payloads and effects with the user before write actions, and require explicit approval before destructive deletes.

## Reference(s):

- [Kernel homepage](https://kernel.sh)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from oo connector commands; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
