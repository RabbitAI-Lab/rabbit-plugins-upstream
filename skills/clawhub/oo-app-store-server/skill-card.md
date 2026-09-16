## Description:

App Store Server API (developer.apple.com). Use this skill for App Store Server API requests, including reading, creating, updating, and deleting data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect live App Store Server API action schemas and run JSON-based operations through an OOMOL-connected account. It supports transaction, subscription, refund, notification, retention messaging, account-token, order lookup, consumption, and test-notification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive App Store Server API operations are routed through a third-party OOMOL connector.

Mitigation: Install and use the skill only when the operator trusts OOMOL with the relevant App Store data and authority.

Risk: Some state-changing or irreversible actions may not be fully covered by the skill's write or destructive labels.

Mitigation: Manually confirm every action that changes state, including renewal extensions, transaction finishing, retention configuration, uploads, deletes, and account-token updates.

Risk: Pipe-to-shell installer commands can execute remote code during CLI setup.

Mitigation: Independently verify the oo CLI source and installer before running pipe-to-shell installation commands.

## Reference(s):

- [App Store Server API Documentation](https://developer.apple.com/documentation/appstoreserverapi)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-app-store-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector commands that return JSON responses with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
