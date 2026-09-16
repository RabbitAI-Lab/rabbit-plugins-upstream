## Description:

Automates App Store Connect requests through OOMOL's app_store_connect connector, including reading, creating, updating, and deleting account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and release operators use this skill to manage App Store Connect through OOMOL, including app metadata, TestFlight, review submissions, pricing, subscriptions, Game Center, certificates, provisioning, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes installer commands that download and immediately run remote scripts.

Mitigation: Install the oo CLI through a verified method, and do not allow an agent to automatically run curl|bash or irm|iex installer commands.

Risk: Write and destructive App Store Connect actions can modify, overwrite, or remove account data.

Mitigation: Review the live schema, target resources, and full payload with the user before execution; require explicit approval for destructive actions.

Risk: Use depends on trusting OOMOL with the App Store Connect workflow.

Mitigation: Install only when OOMOL is trusted for the workflow, and confirm the connected App Store Connect account and scopes before sensitive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [App Store Connect](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents are directed to inspect the live connector schema before constructing JSON payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
