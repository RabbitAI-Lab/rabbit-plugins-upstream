## Description:

Helps agents retrieve App Store Connect app, build, TestFlight, review, sales, and team information and perform confirmed management actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and App Store Connect team members use this skill to inspect apps, TestFlight builds and testers, customer reviews, sales reports, and team users, and to request confirmed updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An overprivileged or exposed App Store Connect API key could expose sensitive app, sales, or team data.

Mitigation: Grant only the roles needed for the workflow and protect the .p8 private key or PEM value.

Risk: Invitations, tester deletion, group changes, beta review submission, or public review responses could have unintended effects.

Mitigation: Review the action preview and confirm the intended target and content before approving each write.

## Reference(s):

- [App Store Connect API documentation](https://developer.apple.com/documentation/appstoreconnectapi)
- [App Store Connect API key setup](https://appstoreconnect.apple.com/access/integrations/api)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/app-store-connect-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can summarize App Store Connect records and reports or draft review responses; write actions require user confirmation.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
