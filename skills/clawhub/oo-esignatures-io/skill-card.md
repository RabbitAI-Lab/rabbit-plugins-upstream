## Description:

This skill helps agents read, create, update, and delete eSignatures.com data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and external users use this skill to operate eSignatures.com through an OOMOL-connected account, including reading contracts and templates, creating contracts and templates, and withdrawing contracts when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Use an official download path, verify integrity when available, and avoid running remote installer scripts blindly.

Risk: Connected accounts can create contracts, create templates, and withdraw contracts.

Mitigation: Confirm write and withdraw payloads with the user before execution, especially target IDs, signer lists, and contract effects.

## Reference(s):

- [eSignatures.com homepage](https://esignatures.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esignatures-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the oo CLI to return JSON responses from eSignatures.com actions.]

## Skill Version(s):

1.0.4 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
