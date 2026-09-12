## Description:

Apple Notary helps agents read, create, and update Apple Notary data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to operate Apple Notary through an OOMOL-connected account, including listing submissions, checking status, retrieving logs, and registering software for notarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands.

Mitigation: Do not let an agent run the installer commands automatically; inspect and validate the script or use a pinned, verified installer.

Risk: The skill mediates Apple Notary operations through OOMOL.

Mitigation: Install only when the user accepts OOMOL-mediated Apple Notary operations and has connected the intended account.

Risk: The submit_software action returns temporary AWS credentials and changes Apple Notary state.

Mitigation: Confirm the exact file hash before submission and treat returned AWS credentials as sensitive until they expire.

## Reference(s):

- [Apple Notary API documentation](https://developer.apple.com/documentation/notaryapi)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Apple Notary skill page](https://clawhub.ai/oomol/skills/oo-apple-notary)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before building action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
