## Description:

Check a proposed purchase against Watchpost merchant signals, listing checks and the user's spending rules before an agent pays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lelis92](https://clawhub.ai/user/lelis92)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill when an agent is preparing a user-requested purchase or subscription and needs a Watchpost verdict before proceeding. It validates purchase input, submits the proposed purchase to Watchpost, and checks authenticated review status when human review is required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchase details and selected listing evidence are sent to Watchpost for review.

Mitigation: Submit only the fields needed for the purchase check and exclude cookies, payment credentials, account pages, hidden authentication fields, and unrelated private data.

Risk: A configured token, local diagnostic, or local validation can be mistaken for purchase approval.

Mitigation: Treat only a valid Watchpost verdict approval for the unchanged purchase as approval, and continue to follow the user's existing authorization and host payment rules.

Risk: Timeouts, rate limits, invalid responses, or inconsistent coverage can leave the purchase unchecked or unconfirmed.

Mitigation: Do not pay on unconfirmed results; inspect the Watchpost dashboard after timeouts and resolve setup or response errors before retrying.

Risk: Human review can be confused with chat approval or reused for a changed or duplicate purchase.

Mitigation: Require approval in the authenticated Watchpost dashboard for the original transaction, recheck the same transaction ID, and submit a new check for changed purchases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lelis92/skills/watchpost)
- [Watchpost homepage](https://watchpost.systems/?ref=clawhub)
- [Watchpost account signup](https://app.watchpost.systems/signup?ref=clawhub)
- [Watchpost connection settings](https://app.watchpost.systems/connections?ref=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON helper results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Purchase checks return structured verdict, review_status, diagnostic, or error JSON; local validation does not approve purchases.]

## Skill Version(s):

0.1.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
