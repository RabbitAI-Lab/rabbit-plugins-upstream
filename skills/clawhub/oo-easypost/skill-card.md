## Description:

This skill helps agents operate EasyPost account workflows through the OOMOL-connected oo CLI, including addresses, trackers, and carrier-type lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations users use this skill to manage EasyPost shipping resources from an agent through an OOMOL-connected account. It supports address creation and retrieval, tracker creation and retrieval, paginated tracker listing, and carrier-type discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute an unverified remote installer directly in a shell.

Mitigation: Review the installer path before installing and prefer a pinned, verifiable package or official instructions with checksums or signatures.

Risk: Write actions can create EasyPost resources in the connected account.

Mitigation: Confirm the exact account, payload, and expected effect with the user before running write actions.

## Reference(s):

- [EasyPost Skill Page](https://clawhub.ai/oomol/skills/oo-easypost)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [EasyPost Homepage](https://www.easypost.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call EasyPost through the oo CLI and may return JSON responses from connector actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
