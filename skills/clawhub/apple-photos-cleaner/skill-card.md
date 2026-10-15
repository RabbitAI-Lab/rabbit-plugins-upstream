## Description:

Helps macOS users analyze and organize Apple Photos libraries by identifying clutter, duplicates, storage usage, and memorable photos, with separately confirmed cleanup and export actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[and3rn3t](https://clawhub.ai/user/and3rn3t)

### License/Terms of Use:

MIT

## Use Case:

Mac users and their agents can review a Photos library for cleanup candidates, storage use, duplicates, and photo highlights before choosing whether to move items to Recently Deleted or export copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports may expose people's names, face-derived details, location history, dates, or shared-library contributor information.

Mitigation: Grant Photos access only if appropriate; treat saved reports as private photo data and avoid sharing them unnecessarily.

Risk: Cleanup moves selected photos to Recently Deleted, and export writes copies to a chosen location.

Mitigation: Review the previewed items and output location, then confirm only the intended cleanup or export action.

## Reference(s):

- [Apple Photos Cleaner on ClawHub](https://clawhub.ai/and3rn3t/skills/apple-photos-cleaner)
- [Workflows](references/workflows.md)
- [Cleanup command guidance](references/commands/cleanup_executor.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Plain-language summaries and command guidance; optional JSON reports or exported photo copies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include personal photo metadata; cleanup and export require preview and explicit confirmation.]

## Skill Version(s):

1.2.0 (source: ClawHub release, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
