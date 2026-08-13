## Description:

Editorial Topic Portfolio evaluates technology, AI, data, cloud, and enterprise-software topic portfolios, applies hard gates and scoring, selects one primary topic with two backups, and prepares confirmed Notion writeback previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, and content strategists use this skill to evaluate a batch of technology-sector topics, decide the current cycle's primary and backup writing candidates, and prepare safe change previews for topic-tracking systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may access private topic files or a Notion topic database during review.

Mitigation: Install only where that access is intended, keep Notion tokens and database IDs in private configuration, and avoid placing private topic data in public skill files.

Risk: Generated portfolio decisions or change previews could be incorrect or misleading if source facts, dates, or status fields are incomplete.

Mitigation: Review the generated portfolio, blockers, scores, and change preview before using them for editorial planning or writeback.

Risk: Notion writeback could update the wrong records or apply changes without adequate authorization.

Mitigation: Require the documented portfolio and writeback confirmations, use stable page IDs rather than title matching, and verify updates through readback after writeback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/editorial-topic-portfolio-skill)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown and JSON reports with inline shell commands and change-preview records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires portfolio confirmation and writeback confirmation before Notion updates; readback verification is expected after writeback.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
