## Description:

Compresses and organizes individual videos or video folders with configurable H.265 or H.264 settings, preview mode, and original-preserving output by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjbook](https://clawhub.ai/user/bjbook)

### License/Terms of Use:

MIT-0

## Use Case:

People managing video libraries can batch transcode videos or organize folders to reduce storage use. They can preview the planned work and keep original files by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crafted filenames can escape the selected output folder when using --out-dir with untrusted files.

Mitigation: Use backed-up copies with restricted write access, and avoid --out-dir for untrusted filenames until output paths are checked for containment.

Risk: Replacement mode can overwrite another video.

Mitigation: Avoid --replace until destination-collision checks are added; use the default original-preserving mode with backed-up copies.

## Reference(s):

- [Project homepage](http://openclaw.bjbook.net/)
- [ClawHub skill page](https://clawhub.ai/bjbook/skills/zhz-video-compress)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Compressed video files and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preserve originals by default or write results to a selected destination.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
