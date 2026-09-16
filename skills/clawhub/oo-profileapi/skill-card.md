## Description:

profileAPI lets agents perform reverse email and E.164 phone lookups through an OOMOL-connected profileAPI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect live profileAPI connector schemas and run reverse email or E.164 phone lookups through the oo CLI with server-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes curl-to-bash and PowerShell-to-iex installer commands that could run unverified remote code.

Mitigation: Prefer an official package manager or a downloaded, versioned installer whose checksum or signature can be verified before installing the oo CLI.

Risk: Reverse email and phone lookups send personal data through the OOMOL profileAPI connector.

Mitigation: Use the skill only for intended profileAPI lookups and submit only personal data the user is authorized to process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-profileapi)
- [profileAPI homepage](https://profileapi.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; lookup outputs may include personal data.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
