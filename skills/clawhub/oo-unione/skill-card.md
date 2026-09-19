## Description:

Operate UniOne through the OOMOL-connected oo CLI for account and project lookup, suppressions, tags, template listing, and transactional email sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run UniOne connector actions through an OOMOL-connected account. It supports reading account/project data, suppressions, tags, and templates, and sending transactional email after reviewing the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review official installation documentation, prefer a package manager or version-pinned installer, and verify signatures or checksums before running setup commands.

Risk: The send_email action can send real transactional email through the user's UniOne account.

Mitigation: Review the exact send_email payload and recipient list with the user before approval.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [UniOne homepage](https://unione.io)
- [ClawHub UniOne skill page](https://clawhub.ai/oomol/skills/oo-unione)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector actions are JSON objects containing data and metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
