## Description:

Docparser (docparser.com). Use this skill for ANY Docparser request — reading, creating, and updating data. Whenever a task involves Docparser, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to automate Docparser workflows through an OOMOL-connected account, including parser discovery, document import, status checks, parsed-result retrieval, re-parsing, and integration queue scheduling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute a remotely fetched installer script without verification.

Mitigation: Install the oo CLI through a verified package or checksum/signature-checked release path before using the skill.

Risk: Write actions can change Docparser document state by uploading, re-parsing, or scheduling integration processing.

Mitigation: Confirm the exact payload and intended effect with the user before running actions tagged as write.

## Reference(s):

- [Docparser Homepage](https://docparser.com)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-docparser)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector commands and live connector schemas; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
