## Description:

Lists saved webcams and retrieves current snapshot JPGs, especially from foto-webcam.eu, for delivery through an agent chat workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unixweb](https://clawhub.ai/user/unixweb)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to list saved webcam favorites and request current webcam snapshots by ID or URL. It supports simple webcam lookup workflows and can prepare image files for delivery through chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The snapshot helper can fetch unrestricted URLs from user-supplied arguments or favorites data.

Mitigation: Keep favorites files limited to trusted webcam URLs and review any direct URL before running the helper.

Risk: The helper writes image bytes to the requested output path.

Mitigation: Use predictable temporary output paths and avoid running the skill with elevated privileges.

Risk: Images may be sent through Telegram as part of the workflow.

Mitigation: Verify the Telegram destination before sending webcam snapshots.

## Reference(s):

- [Photo Webcam skill page](https://clawhub.ai/unixweb/skills/photo-webcam)
- [unixweb publisher profile](https://clawhub.ai/user/unixweb)
- [foto-webcam.eu example webcam page](https://www.foto-webcam.eu/webcam/zugspitze/)

## Skill Output:

**Output Type(s):** [text, shell commands, code, configuration]

**Output Format:** [Plain text guidance, JSON script output, and JPG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The snapshot helper writes a JPG to a requested output path and prints one JSON status line.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
