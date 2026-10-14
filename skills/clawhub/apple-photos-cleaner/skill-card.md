## Description:

Helps macOS users inspect and organize Apple Photos libraries with local reports on clutter, duplicates, storage, and photo activity, plus optional cleanup and export actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[and3rn3t](https://clawhub.ai/user/and3rn3t)

### License/Terms of Use:

MIT

## Use Case:

People and their assistants use this skill on macOS to review a Photos library, identify cleanup candidates, understand storage and photo history, and plan exports before approving changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local reports and terminal output may expose names, faces, locations, habits, or shared-library contributor details.

Mitigation: Limit access to the Photos library and treat reports and terminal output as private; review where reports are saved or shared.

Risk: Cleanup can move photos to Recently Deleted, and export can create copies outside the library.

Mitigation: Preview cleanup and export plans before approval; grant Photos automation access only when needed.

## Reference(s):

- [Apple Photos Cleaner on ClawHub](https://clawhub.ai/and3rn3t/skills/apple-photos-cleaner)
- [Photos database schema reference](references/database-schema.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, JSON reports]

**Output Format:** [Markdown guidance and local JSON or human-readable reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may contain sensitive photo metadata; cleanup and export require explicit user approval.]

## Skill Version(s):

1.0.3 (source: frontmatter, pyproject.toml, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
