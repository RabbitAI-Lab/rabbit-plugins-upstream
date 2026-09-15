## Description:

VerifiedEmail (verified.email) helps an agent inspect schemas and run VerifiedEmail account actions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to verify email addresses, inspect VerifiedEmail action schemas, retrieve verification lists and downloads, and check account entitlements through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute network responses in a shell.

Mitigation: Review the setup path before installation and prefer official, version-pinned OOMOL CLI installation instructions with checksum or signature verification.

Risk: Email verification requests may expose email addresses to the VerifiedEmail service and consume account credits.

Mitigation: Connect only the intended VerifiedEmail account and confirm verification payloads, especially before running verify_emails.

Risk: Incorrect action payloads could produce failed or unintended connector requests.

Mitigation: Inspect the live action schema with oo connector schema before constructing each request.

## Reference(s):

- [ClawHub VerifiedEmail Skill Listing](https://clawhub.ai/oomol/skills/oo-verifiedemail)
- [VerifiedEmail Homepage](https://verified.email)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
