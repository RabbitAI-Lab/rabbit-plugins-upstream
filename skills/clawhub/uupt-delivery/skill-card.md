## Description:

UU Paotui same-city delivery skill for courier and on-site help services, including price quotes, order creation, order lookup, cancellation, and driver tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uupt-mcp](https://clawhub.ai/user/uupt-mcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask an agent to arrange same-city courier delivery, on-site assistance, order pricing, order management, and driver tracking through UU Paotui service flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create paid delivery or help-service orders without a final confirmation step.

Mitigation: Require explicit user confirmation immediately before order creation, including price, destination or service location, recipient phone, and payment implications.

Risk: The skill can silently replace its own code from a remote update source and run dependency installation.

Mitigation: Disable silent self-update, pin reviewed release hashes, and require manual approval before replacing files or installing dependencies.

Risk: The skill stores service credentials in the user's home directory and can contact third-party IP and QR-code services.

Mitigation: Limit credential scope, protect local configuration files, disclose external network calls, and allow users to opt out or provide values manually.

## Reference(s):

- [UU Paotui Open Platform](https://open.uupt.com)
- [ClawHub Skill Page](https://clawhub.ai/uupt-mcp/skills/uupt-delivery)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON/API result snippets, and local configuration or payment files when required.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May store UU Paotui credentials under the user's home directory and may emit payment links, order identifiers, or QR-code image paths.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter and package.json report 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
