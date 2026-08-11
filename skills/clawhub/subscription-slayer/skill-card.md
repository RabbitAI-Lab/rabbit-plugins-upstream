## Description:

Tracks subscriptions, calculates monthly and annual costs, detects likely-unused services based on last-used patterns, and generates ready-to-send cancellation email templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to audit recurring subscription spending, rank subscriptions by likely waste, and draft cancellation emails for subscriptions the user chooses to review or cancel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Subscription JSON can contain financial and account-related information.

Mitigation: Keep subscription files local and avoid sharing them with untrusted systems or recipients.

Risk: Generated cancellation emails may include guessed support addresses and account placeholders.

Mitigation: Verify the recipient address and replace all placeholders with correct account details before sending.

Risk: Waste scores are heuristic and depend on user-provided last-used dates, categories, and subscription data.

Mitigation: Review recommendations against actual usage and billing records before cancelling a service.

## Reference(s):

- [Waste Detection Methodology](references/waste_detection.md)
- [Cancellation Email Template Reference](references/cancellation_template.md)
- [Server-resolved GitHub Source](https://github.com/voronindenis5/subscription-slayer)
- [ClawHub Skill Listing](https://clawhub.ai/voronindenis5/skills/subscription-slayer)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Plain text or JSON analysis, plus markdown-style cancellation email drafts and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on user-provided subscription JSON and local heuristic scoring; generated cancellation emails include placeholders that must be reviewed before use.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
