## Description:

Doppler Marketing Automation helps an agent read, create, update, and delete Doppler Email Marketing lists and subscribers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Doppler Email Marketing subscriber lists and list memberships through the OOMOL oo CLI. It supports read actions directly and requires confirmation before write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly.

Mitigation: Install only after verifying the oo CLI through trusted OOMOL sources, preferably with a signed package, pinned release, or reviewed download script.

Risk: Write and destructive actions can change Doppler lists or remove subscriber memberships.

Mitigation: Approve these actions only after checking the exact target, payload, and expected effect with the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-doppler-marketing-automation)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Doppler Marketing Automation Homepage](https://www.fromdoppler.com/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
