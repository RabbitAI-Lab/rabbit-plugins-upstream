## Description:

Helps agents access App Store Connect apps, TestFlight builds and testers, customer reviews, reports, and team users, with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store Connect team members use this skill to check apps, builds, testers, reviews, reports, and team users, and to manage TestFlight and account workflows with approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to business data and account or TestFlight changes through an Apple API key.

Mitigation: Use a least-privilege API key and grant access only when App Store Connect work is intended.

Risk: Exposing the private API key in a chat or configuration exchange.

Mitigation: Use a local private-key file path instead of pasting the key into a chat.

Risk: Unintended tester, review, team-user, or beta-review changes.

Mitigation: Review each confirmation preview and approve only the intended changes.

## Reference(s):

- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API key setup](https://appstoreconnect.apple.com/access/integrations/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include App Store Connect data and confirmation previews before account or TestFlight changes.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
