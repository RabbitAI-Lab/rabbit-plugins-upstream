## Description:

This skill helps agents upscale product videos, enhance clarity, interpolate frames, and preserve audio-video synchronization through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and commerce teams use this skill to improve blurry, low-bitrate, compressed, or older product videos. It is suited for short video enhancement workflows that need clearer frames, smoother motion, and synchronized audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and uses the Qinghu qhkit CLI and requires a Qinghu API key.

Mitigation: Install the CLI only in environments where this dependency is acceptable, and provide credentials only through the documented Qinghu configuration flow.

Risk: Selected videos are uploaded to Qinghu's service for processing.

Mitigation: Use only videos that the user owns or is authorized to process, and avoid uploading sensitive or restricted media unless Qinghu's service terms are acceptable.

Risk: Generation can consume paid Qinghu credits.

Mitigation: Run an estimate first, present the expected credit use to the user, and submit generation only after explicit approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-video-upscale-hd)
- [ClawHub Publisher Profile](https://clawhub.ai/user/autoagc)
- [Qinghu qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents through option lookup, credit estimation, user confirmation, task submission, polling, and final video delivery.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
