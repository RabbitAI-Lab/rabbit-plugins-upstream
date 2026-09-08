## Description:

Turn Xiaohongshu hall FAQ complaints into a 4 to 8 still materials set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hall or public-service teams use this skill to convert Xiaohongshu hall FAQ complaints and confirmed official document facts into 4 to 8 materials stills or checklist-style cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device credential with permissions beyond still-image generation.

Mitigation: Review the Beatra approval page before allowing access, use the bundled authorization and uninstall workflows, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: Automatic package updates are enabled silently by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before normal use if unattended package replacement is not acceptable.

Risk: Paid lookup, generation, transform, and edit tasks can consume credits or duplicate work if replayed incorrectly.

Mitigation: Use one opaque `client_request_id` per approved operation, retry only byte-identical requests with the same ID during transport uncertainty, and report final `billing.net_charged_credits` from terminal task results.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-hall-faq-stills)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-hall-faq-stills)
- [Hall FAQ still workflow](references/workflow.md)
- [Xiaohongshu hall FAQ lookup](references/hall-faq-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans complaint-to-materials slots first, then may produce Beatra task results and generated image artifact details after user approval.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
