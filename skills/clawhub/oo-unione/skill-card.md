## Description:

UniOne helps agents read, create, and update UniOne data through the OOMOL-connected unione connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate UniOne account, suppression, tag, template, and transactional email workflows through the oo CLI while relying on live connector schemas for payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that download and execute code.

Mitigation: Review the installer source before running it, or prefer a verified, pinned, package-manager installation path.

Risk: The send_email action changes state by sending transactional email through UniOne.

Mitigation: Inspect the live connector schema and confirm the exact payload, recipient, and effect with the user before running the write action.

## Reference(s):

- [ClawHub UniOne skill page](https://clawhub.ai/oomol/skills/oo-unione)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [UniOne homepage](https://unione.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
