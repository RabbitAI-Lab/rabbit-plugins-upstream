## Description:

Edits talking-head footage with gtrk by aligning separate speech audio when present, removing retakes and long pauses, and producing editable project files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gitruck](https://clawhub.ai/user/gitruck)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video editors use this skill to turn talking-head footage into an editable rough cut, synchronize separate speech audio when available, and prepare projects for supported editing applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may start additional production work beyond the requested edit.

Mitigation: Keep work within the requested editing project and get approval before creating a storyboard or continuing production.

Risk: Extracted audio, supplied script text, and an optional video proxy may be sent to the cloud service, and cloud use may consume account credit.

Mitigation: Explain the expected uploads and possible credit use before starting cloud processing.

Risk: Installing video tools from an untrusted source or relying on an unverified checksum could introduce unsafe binaries.

Mitigation: Use trusted dependency downloads and independently sourced checksums.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/gitruck/skills/gtrk-oralcut)
- [Gitruck CLI homepage](https://github.com/Gitruck/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video editing project files, Video files]

**Output Format:** [gtrk project, Jianying draft, Premiere XML, and optionally rendered MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project formats depend on the selected options; MP4 rendering is optional.]

## Skill Version(s):

1.3.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
