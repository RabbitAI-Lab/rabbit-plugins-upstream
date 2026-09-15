## Description:

Docparser (docparser.com). Use this skill for ANY Docparser request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Docparser through an OOMOL-connected account, including listing parsers, reading document results and statuses, and queuing supported document actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands for the oo CLI.

Mitigation: Do not let an agent run installer commands automatically; install the oo CLI only through a trusted process with version pinning and checksum or signature verification where available.

Risk: Docparser actions can upload files or trigger reparse and reintegration workflows that change account state.

Mitigation: Confirm the exact parser, document identifiers, payload, and intended effect with the user before upload, reparse, reintegrate, or other write actions.

## Reference(s):

- [Docparser homepage](https://docparser.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docparser)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Docparser connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
