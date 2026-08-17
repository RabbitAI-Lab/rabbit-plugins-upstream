## Description:

Tracks subscriptions, calculates monthly and annual costs, detects likely-unused services based on last-used patterns, and generates ready-to-send cancellation email templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to audit recurring subscription costs, rank likely-unused services, and draft cancellation emails for subscriptions the user chooses to stop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cancellation drafts can contain guessed recipient addresses, placeholders, or wording that may not fit a provider or location.

Mitigation: Verify the recipient address, replace all placeholders, and review provider-specific and local requirements before using any cancellation message.

Risk: Heuristic waste scores can misclassify subscriptions when last-used dates, categories, or user needs are incomplete.

Mitigation: Review the underlying subscription data and personal need for each service before acting on a cancellation recommendation.

Risk: The workflow may handle subscription, account, and contact details supplied by the user.

Mitigation: Provide only the data needed for analysis and review generated drafts before sharing them outside the local workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/subscription-slayer)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/subscription-slayer)
- [Waste Detection Methodology](references/waste_detection.md)
- [Cancellation Email Template Reference](references/cancellation_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Terminal text or JSON summaries with markdown-style cancellation email drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided subscription JSON and includes placeholders that must be reviewed before any cancellation message is sent.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
