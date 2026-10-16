## Description:

Creates a read-only PikPak storage report covering capacity, folder sizes, largest files, and potential cleanup opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users can review storage usage, identify large folders and files, and decide what to clean up without the skill deleting anything.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storage scans and saved JSON reports can expose private file and folder names, sizes, IDs, and timestamps.

Mitigation: Use only when comfortable sharing PikPak storage metadata with the agent; review or delete saved reports such as /tmp/pikpak-storage.json.

Risk: Usage figures and potential cleanup estimates may become stale or overstate what can be freed.

Mitigation: Treat the report as a point-in-time snapshot and confirm cleanup decisions yourself; the skill does not delete files.

## Reference(s):

- [PikPak Storage Report on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-storage-report)
- [PikPak CLI installation](https://mypikpak.com/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Human-readable storage report with optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only snapshot; optional JSON report includes file and folder metadata.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
