## Description:

VerifiedEmail (verified.email) lets an agent inspect VerifiedEmail action schemas, verify email addresses, and retrieve verification-related account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with VerifiedEmail through an OOMOL-connected account, including schema inspection, synchronous verification of up to 10 email addresses, and retrieval of lists, downloads, entitlements, and related account state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts in a shell.

Mitigation: Review the oo CLI installer through a safer channel, prefer a package manager or signed and pinned release, and avoid piping downloaded scripts directly into a shell.

Risk: VerifiedEmail tasks route requested email addresses through OOMOL and the VerifiedEmail service.

Mitigation: Send only email addresses appropriate for that connected service and confirm privacy or data-handling requirements before verification.

## Reference(s):

- [VerifiedEmail homepage](https://verified.email)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-verifiedemail)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; VerifiedEmail command responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: skill metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
