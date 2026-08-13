## Description:

Tracks subscriptions, calculates monthly and annual costs, detects likely-unused services based on last-used patterns, and generates ready-to-send cancellation email templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to audit user-provided subscription data, estimate wasted spend, and prepare cancellation email drafts for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subscription data may include personal financial details.

Mitigation: Include only the fields needed for analysis, avoid account IDs or private notes unless necessary, and treat the JSON file as sensitive personal data.

Risk: Generated cancellation emails may include placeholders, inferred recipient addresses, or wording that does not fit the user's jurisdiction or account.

Mitigation: Review every cancellation draft, recipient address, account identifier, and legal phrase before sending it yourself.

Risk: Waste scores are heuristic and depend on user-provided last-used dates, categories, costs, and billing cycles.

Mitigation: Confirm the underlying subscription details and personal need for each service before cancelling.

## Reference(s):

- [Waste Detection Methodology](references/waste_detection.md)
- [Cancellation Email Template Reference](references/cancellation_template.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/subscription-slayer)
- [Source Repository](https://github.com/voronindenis5/subscription-slayer)
- [Imported Commit](https://github.com/voronindenis5/subscription-slayer/commit/3889d104abe5f7159f9c6a34033b5de3200d6871)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, shell commands, guidance]

**Output Format:** [Plain text or JSON subscription reports, Markdown-style cancellation email drafts, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided JSON input; cancellation drafts include placeholders and inferred recipient addresses that must be reviewed before sending.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence; SKILL.md frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
