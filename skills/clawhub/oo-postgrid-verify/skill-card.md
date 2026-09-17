## Description:

PostGrid Verify helps agents autocomplete, parse, look up, verify, and standardize US and Canadian addresses through an OOMOL-connected PostGrid Verify account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to run PostGrid Verify address autocomplete, city/state lookup, freeform parsing, and US or Canadian address verification from an agent through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup documents remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI through a verifiable official release or package manager; do not let an agent run the documented remote installer commands directly.

Risk: The skill depends on OOMOL as the PostGrid Verify connector and may send address payloads through that connected account.

Mitigation: Install only if OOMOL is an acceptable connector for the deployment, and confirm account connection and payload details before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-postgrid-verify)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [PostGrid Verify homepage](https://www.postgrid.com/address-verification/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
