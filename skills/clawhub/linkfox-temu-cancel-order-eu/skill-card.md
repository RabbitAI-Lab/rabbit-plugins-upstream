## Description:

Helps agents call LinkFox gateway scripts for Temu Partner EU order-cancellation workflows, including buyer after-sales cancellation and seller appeal or out-of-stock cancellation APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agent developers use this skill to prepare and run Temu EU cancellation requests through LinkFox, using either direct Temu access tokens or saved store keys. It supports buyer cancellation review and approval plus seller appeal and out-of-stock cancellation flows.

### Deployment Geography for Use:

Europe for Temu Partner EU workflows; otherwise Global for skill execution unless local policy restricts use.

## Known Risks and Mitigations:

Risk: The release was flagged suspicious because it combines a legitimate Temu EU cancellation workflow with broader proxy, file-download, token-management, onboarding, billing, and persistence behavior.

Mitigation: Review the skill before installation and use only the scripts needed for the intended Temu EU cancellation task.

Risk: The skill requires LinkFox and Temu credentials, including access tokens or saved store keys.

Mitigation: Treat all LinkFox and Temu tokens as secrets, prefer environment variables or a private token store, and avoid storing token files in shared or synced directories.

Risk: Cancellation APIs can change real order state or submit cancellation-related requests.

Mitigation: Require human confirmation before order-canceling actions and verify parent order, after-sales, apply, and child order identifiers before execution.

Risk: Scripts persist full JSON responses locally, which may include order, shop, or customer-related data.

Mitigation: Run the skill from a private workspace, review saved response paths, and avoid sharing or syncing generated linkfox session data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-eu)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Skill definition](artifact/SKILL.md)
- [API reference](artifact/references/api.md)
- [Temu access token guide](artifact/references/access-token.md)
- [Partner EU cancellation catalog](artifact/references/partner-eu-catalog.md)
- [Endpoint documentation index](artifact/references/apis/README.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Files, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full JSON responses under a linkfox session data directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
