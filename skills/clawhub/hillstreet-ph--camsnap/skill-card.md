## Description:

Capture frames or clips from RTSP/ONVIF cameras and local webcams, including USB pan/tilt/zoom control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and camera operators use camsnap to discover configured cameras and capture snapshots, video clips, or motion events. On macOS, they can also inspect and control supported local webcam PTZ devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The camera configuration contains camera credentials.

Mitigation: Restrict access to the configuration file and use dedicated camera credentials where possible.

Risk: The motion watch command accepts an action to run when motion is detected.

Mitigation: Review the configured action and its effects before enabling motion watch.

## Reference(s):

- [camsnap homepage](https://camsnap.ai)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [Image snapshots and video clips, with shell command examples and YAML configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Capture device, duration, output path, motion threshold, and PTZ settings are selected through commands.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
