## Description:

Create Douyin live-commerce visuals from a livestream theme, product details, product photos, and brand references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and agents use this skill to plan and produce a coordinated Douyin live-commerce visual kit: a pre-live promo cover, product selling-point card, and live-room background or overlay visual. It also guides confirmation, Beatra task submission, task recovery, and delivery of title and on-screen copy options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization for media generation, wallet spending, task access, artifacts, cancellation, and related tool access.

Mitigation: Install only if that authorization is acceptable, keep the local credential private, use it only with media intended for Beatra, and revoke the device connection when it is no longer needed.

Risk: The bundled client checks for and installs package updates automatically by default.

Mitigation: Run `python3 scripts/mcp_client.py update --auto off` to disable silent automatic updates, or use `python3 scripts/mcp_client.py update --check` to review available updates before installing.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/douyin-live-commerce-visual-kit)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-live-commerce-visual-kit)
- [Douyin live-commerce visual workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of three named visual deliverables and related copy; remote image tasks return Beatra task and artifact references.]

## Skill Version(s):

0.1.1 (source: server release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
