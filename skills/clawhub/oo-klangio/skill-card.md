## Description:

Klangio connector for reading, creating, and updating Klangio data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Klangio audio-processing workflows from an OOMOL-connected account, including creating transcription, beat, chord, strum, and source-separation jobs, checking job status, and downloading generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through an official or verified method and inspect installer payloads before execution.

Risk: Write actions can create Klangio processing jobs from user-supplied audio URLs or Base64 audio and may upload generated outputs to OOMOL transit storage.

Mitigation: Fetch the live action schema, confirm exact payloads and effects with the user, and run write actions only after approval.

## Reference(s):

- [Klangio homepage](https://klang.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Klangio skill page](https://clawhub.ai/oomol/skills/oo-klangio)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
