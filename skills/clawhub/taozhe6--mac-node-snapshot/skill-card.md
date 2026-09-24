## Description:

A macOS screen capture skill that records a short OpenClaw screen.record clip and extracts a high-quality PNG frame for reliable snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[taozhe6](https://clawhub.ai/user/taozhe6)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to capture the visible macOS screen when a user asks for a screenshot or screen inspection, especially when direct screenshot utilities are unreliable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can capture sensitive visible screen contents and save them as local MP4 and PNG files.

Mitigation: Close or hide private windows before use and delete the temporary capture files after they are no longer needed.

Risk: Screen capture may fail or return a black frame if macOS Screen Recording permission is missing or the screen is asleep or locked.

Mitigation: Grant Screen Recording permission when required, keep the screen awake, and retry the capture.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown with inline bash code blocks and local MP4/PNG capture files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OpenClaw screen.record access and ffmpeg; saves temporary capture files under the skill tmp directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
