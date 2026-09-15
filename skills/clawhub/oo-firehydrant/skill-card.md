## Description:

FireHydrant helps agents operate FireHydrant through an OOMOL-connected account for reading, creating, and updating incident, service, and environment data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and incident responders use this skill to inspect FireHydrant incidents, services, and environments, and to create incidents through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes a remote shell installer for the oo CLI.

Mitigation: Install the oo CLI from a trusted, verified source and do not allow an agent to run the remote installer automatically.

Risk: The create_incident action changes FireHydrant state.

Mitigation: Fetch the live connector schema, present the exact incident payload and expected effect, and get user confirmation before execution.

## Reference(s):

- [ClawHub FireHydrant skill page](https://clawhub.ai/oomol/skills/oo-firehydrant)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [FireHydrant homepage](https://firehydrant.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
