## Description:

Scans PikPak cloud-drive folders for promotional junk files, presents a tiered report, and guides user-approved moves to the trash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can scan cloud-drive folders for unwanted promotional files bundled with downloads, review a categorized list, and explicitly approve which files to move to the trash.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Promotional-file classification may flag legitimate files for cleanup.

Mitigation: Review the proposed file list, especially review-tier files, and confirm each selected file before moving it to trash.

Risk: Cleanup commands could target unintended files or a broader folder than intended.

Mitigation: Verify the PikPak folder and generated pikpak rm IDs before approving any cleanup; do not use it for generic local downloads cleanup.

## Reference(s):

- [PikPak Ad Cleaner on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-ad-cleaner)
- [PikPak CLI installation](https://mypikpak.com/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [Categorized Markdown summary, optional JSON report, and optional pikpak rm commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports high-confidence, review-required, and protected files; cleanup requires explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
