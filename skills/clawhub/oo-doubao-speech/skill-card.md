## Description:

Doubao Speech access through OOMOL for reading, creating, and updating Doubao Speech data without calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Doubao Speech action schemas, submit asynchronous speech-to-text and text-to-speech tasks, and retrieve task status and outputs through the OOMOL-connected oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line installers that run code from the internet.

Mitigation: Review the installer path before installing and prefer a signed, versioned, or checksum-verified oo CLI installation method.

Risk: Connected OOMOL accounts can be used to submit Doubao Speech write actions.

Mitigation: Only connect accounts acceptable for OOMOL-mediated use and confirm exact payloads before running write actions.

## Reference(s):

- [Doubao Speech skill page](https://clawhub.ai/oomol/skills/oo-doubao-speech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Doubao Speech homepage](https://www.volcengine.com/product/doubao-voice)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action requests; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
