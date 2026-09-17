## Description:

Apple Notary helps agents read, create, and update Apple Notary submissions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to inspect Apple Notary action schemas, submit software for notarization, check submission status, list recent submissions, and retrieve notarization logs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the skill before installing, independently trust and verify the oo CLI installer source, and prefer a signed or checksum-verified installation path.

Risk: The submit_software action changes Apple Notary state and returns temporary upload credentials for a notarization workflow.

Mitigation: Confirm the exact payload and intended effect with the user before submitting software, then poll status and review the notarization log.

## Reference(s):

- [ClawHub Apple Notary Skill](https://clawhub.ai/oomol/skills/oo-apple-notary)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Apple Notary API Documentation](https://developer.apple.com/documentation/notaryapi)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before payload construction; state-changing notarization submissions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
