## Description:

Monitor and track unauthorized content republication across the web. Generates cease-and-desist letters, manages canonical tags, and maintains attribution records. Use when the user needs content protection, copyright enforcement, or citation management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ncreighton](https://clawhub.ai/user/ncreighton)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, publishers, and content teams use this skill to monitor content reuse, track attribution, generate enforcement drafts, manage canonical tags, and prepare compliance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated enforcement letters or takedown notices could be sent without adequate legal review.

Mitigation: Require manual approval by the user or counsel before sending notices, filing takedowns, or routing documents for signature.

Risk: Canonical-tag changes or WordPress updates could alter live website behavior.

Mitigation: Review proposed changes, test on a staging copy where possible, and require explicit approval before modifying production content.

Risk: Large scheduled scans can create operational load or broad monitoring activity beyond the intended content library.

Mitigation: Limit scan scope, set clear schedules and thresholds, and prefer detection-only reporting until the user confirms follow-up actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ncreighton/skills/attribution-content-credit-tracker)
- [Google Programmable Search Engine](https://programmablesearchengine.google.com/)
- [Copyscape API](https://www.copyscape.com/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON reports, HTML snippets, plain-text legal drafts, shell command examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference external search, plagiarism detection, legal-template, notification, and website-management services when configured by the user.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
