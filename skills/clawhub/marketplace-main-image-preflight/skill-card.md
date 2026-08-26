## Description:

Review an existing product main image for Amazon, Shopify, Etsy, or another marketplace and turn target listing requirements into a clear preflight card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and listing operators use this skill to evaluate one existing marketplace main image against a named marketplace, region, and category, prepare a preflight card, and run one seller-approved cleanup edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security guidance says the package uses a shared Device Token with broader media and wallet permissions than this one image workflow needs.

Mitigation: Install only if that account-level access is acceptable, keep the token out of chat and logs, and review or revoke Beatra account/device access from the console when access is no longer needed.

Risk: The security guidance says product images may be uploaded to Beatra for paid processing after approval.

Mitigation: Confirm the preflight card, repair prompt, base image, output count, and price information before approving the single paid edit.

Risk: The security summary says silent package updates are enabled by default.

Mitigation: Use the documented update command to disable automatic updates before use when change control is required.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/marketplace-main-image-preflight)
- [Beatra skill homepage](https://beatra.ai/skills/marketplace-main-image-preflight)
- [Main image preflight workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Image artifacts]

**Output Format:** [Markdown preflight card, command arguments, task and result details, and one edited image artifact when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes approval-gated paid work, task IDs, resolved model details, output dimensions, and net charged credits when an edit is executed.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
