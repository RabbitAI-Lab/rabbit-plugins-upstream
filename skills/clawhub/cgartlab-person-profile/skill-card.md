## Description:

Creates, maintains, standardizes, and validates evidence-grounded person profiles, including reciprocal links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cgartlab](https://clawhub.ai/user/cgartlab)

### License/Terms of Use:

MIT-0

## Use Case:

People maintaining personal knowledge bases use this skill to create, update, standardize, and validate structured profiles. It supports evidence-based research and drafting, reciprocal relationship links, and archive quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bulk edits or heading migrations could affect unintended profile files.

Mitigation: Select only the intended profile directory, keep a backup, run migration with --dry-run, and review the report before approving changes.

Risk: Private profile material could be exposed when shared with an AI service or published.

Mitigation: Review and remove private material before sharing; treat any suggestion involving email access or publishing as a separate decision.

## Reference(s):

- [CGArtLab Person Profile on ClawHub](https://clawhub.ai/cgartlab/skills/cgartlab-person-profile)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown person profiles and reports, with shell commands or code when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update profile files and indexes after user approval.]

## Skill Version(s):

0.2.1 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
