## Description:

Analyzes Apple Photos libraries on macOS to identify cleanup candidates, review storage and photo activity, and plan opt-in exports or cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[and3rn3t](https://clawhub.ai/user/and3rn3t)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and their agents use this skill to find duplicate or unwanted photos, understand storage and library trends, and review cleanup or export plans before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may expose names, face data, locations, travel patterns, or shared-library contributors.

Mitigation: Keep reports private, prefer on-screen summaries, and save JSON only when necessary.

Risk: Cleanup moves photos to Recently Deleted and exports write copies to disk.

Mitigation: Preview and review plans first; grant Photos.app Automation access or confirm cleanup only when intended.

## Reference(s):

- [Apple Photos Cleaner on ClawHub](https://clawhub.ai/and3rn3t/skills/apple-photos-cleaner)
- [Photos database schema reference](references/database-schema.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands; scripts return JSON or human-readable text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis is read-only; exports and cleanup are separate opt-in actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release, frontmatter, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
