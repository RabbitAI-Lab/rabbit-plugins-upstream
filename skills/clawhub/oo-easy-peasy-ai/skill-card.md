## Description:

Helps agents list and inspect Easy-Peasy.AI text presets and generate text through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People using Easy-Peasy.AI can discover text-generation presets, review their required inputs, and generate text through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running a remote installation script directly in a shell.

Mitigation: Install the OOMOL CLI only from a trusted source; prefer verified installer instructions with checksums or signatures over running a fetched script.

Risk: Text generation can consume credits on the connected account.

Mitigation: Confirm the exact generation request and intended account before submitting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oomol/skills/oo-easy-peasy-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Easy-Peasy.AI](https://easy-peasy.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown; connector responses in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text generation may consume account credits.]

## Skill Version(s):

1.0.0 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
