## Description:

GitHub Project Radar helps agents deduplicate GitHub repository candidates, classify them into use, publish, test, or archive tiers, and maintain a local review table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

Developers, content creators, researchers, and operators use this skill to turn incoming GitHub repository links into a consistent candidate record with deduplication, tiering, next actions, and review notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose installing or runtime testing third-party repositories before their commands and cleanup paths are understood.

Mitigation: Only allow installation or runtime testing after reviewing the source command, expected result, rollback plan, and giving explicit approval.

Risk: Candidate table write-back can introduce duplicate, stale, or incorrect records if repository links are not canonicalized.

Mitigation: Normalize each repository to owner/repo, check existing records first, and update last_seen or review notes instead of creating another row for the same repository.

## Reference(s):

- [Review Checklist](references/review-checklist.md)
- [Candidate Table Template](assets/candidate-table-template.md)
- [ClawHub Skill Page](https://clawhub.ai/shiyan521/skills/github-project-radar)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown candidate records and review notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update or populate a local candidate table when the user provides one.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
