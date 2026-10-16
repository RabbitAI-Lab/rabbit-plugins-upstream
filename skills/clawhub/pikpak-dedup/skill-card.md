## Description:

Identifies likely duplicate or alternate-version files in a PikPak folder and recommends which to keep or move to trash after user review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents review likely duplicate or alternate-version files, choose which copies to keep, and approve any move-to-trash commands before cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filename and metadata matches may group distinct files, especially when scanning the root folder or across different collections.

Mitigation: Review each proposed duplicate and its folder before approving cleanup; do not treat a different version as an identical copy.

Risk: Approving a trash command for the wrong file could remove a wanted copy from the active drive.

Mitigation: Confirm the proposed file IDs and keep choices before running any pikpak rm command; analysis alone does not move files.

## Reference(s):

- [PikPak Dedup on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-dedup)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown duplicate-group summary, JSON analysis report, and optional PikPak trash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keep recommendations follow the selected newest, largest, or highest-resolution policy; trash commands require user approval.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
