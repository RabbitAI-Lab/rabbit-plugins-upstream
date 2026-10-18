## Description:

Guides agents in identifying and removing AI watermarks and provenance marks from images and videos that users are authorized to modify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wiltodelta](https://clawhub.ai/user/wiltodelta)

### License/Terms of Use:

Apache-2.0

## Use Case:

Creators and developers use this skill to inspect AI provenance signals and, where authorized, remove AI labels or metadata from their own images and videos.

### Deployment Geography for Use:

Global; removal is subject to local restrictions, including those noted for mainland China.

## Known Risks and Mitigations:

Risk: Installing or upgrading dependencies, overwriting media, or processing directories may have unintended effects.

Mitigation: Review proposed installations and bulk operations, use a separate output path, and confirm results before relying on them.

Risk: Removing provenance from media without permission or presenting generated work as human-made can mislead others or violate restrictions.

Mitigation: Limit removal to media the user is allowed to modify, refuse third-party paid-asset marks and deceptive origin claims, and check applicable local rules.

Risk: A missing local provenance signal may be mistaken for proof that media is human-made or watermark-free.

Mitigation: Report inconclusive findings as unknown and describe only the changes actually confirmed by the tool.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wiltodelta/skills/remove-ai-watermarks)
- [Project website](https://raiw.cc)
- [Project repository (skill metadata)](https://github.com/wiltodelta/remove-ai-watermarks)
- [Command recipes](references/commands.md)
- [Installation guidance](references/install.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports observed command results and output paths; an absent local signal is not proof of human origin.]

## Skill Version(s):

1.0.12 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
