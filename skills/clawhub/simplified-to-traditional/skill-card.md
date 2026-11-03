## Description:

Converts a user-selected Simplified Chinese article into a Taiwan-style Traditional Chinese Markdown twin, adds cross-links, and provides a workflow for keeping the pair synchronized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and writers use this skill when they explicitly request a Traditional Chinese version of a named Simplified Chinese article. It creates and maintains the paired Markdown files with cross-links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Direct script execution overwrites the Traditional file without prompting, and also updates the source cross-link.

Mitigation: Confirm the source and output paths and overwrite status with the user, and keep recoverable copies of both documents.

Risk: Conversion can choose the wrong Traditional form for ambiguous characters or alter wording inside quotations.

Mitigation: Review converted text, compare quotations with their cited editions, and verify the script's ambiguous-form warnings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [Traditional Chinese Markdown article with cross-links and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Acts only on a user-named article after explicit approval; does not backfill existing articles automatically.]

## Skill Version(s):

1.0.8 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
