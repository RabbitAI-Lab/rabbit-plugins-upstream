## Description:

profileAPI helps agents query profileAPI through the OOMOL oo CLI for reverse email and phone lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run profileAPI lookups through an OOMOL-connected account. It supports reverse lookup by email address or E.164 phone number and returns profileAPI results through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs can include personal data such as email addresses or phone numbers that are sent to OOMOL/profileAPI.

Mitigation: Use the skill only for explicit profileAPI lookup requests and avoid submitting data that the user has not authorized for lookup.

Risk: Setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Prefer a verified installer, package manager, checksum, or signature from the publisher before installing the oo CLI.

## Reference(s):

- [profileAPI ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-profileapi)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [profileAPI Homepage](https://profileapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
