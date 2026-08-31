## Description:

Turn Xiaohongshu hall FAQ complaints into a 4 to 8 still materials set from confirmed document facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hall or public-service teams use this skill to turn pasted or looked-up Xiaohongshu hall FAQ complaints and confirmed document facts into a reviewed materials still pack.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device authorization broader than still-image creation.

Mitigation: Review the authorization before installing, keep the device token private, and reconnect only when the user explicitly chooses to do so.

Risk: Package-owned automatic updates are enabled silently by default.

Mitigation: Disable automatic updates for the installation with `python3 scripts/mcp_client.py update --auto off` when silent updates are not acceptable.

Risk: Lookup and image operations can consume Beatra credits.

Mitigation: Use the skill's separate confirmation cards for lookup, generate, transform, and edit stages, and report terminal billing truth from returned task data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/xiaohongshu-hall-faq-stills)
- [Beatra skill homepage](https://beatra.ai/skills/xiaohongshu-hall-faq-stills)
- [Hall FAQ still workflow](references/workflow.md)
- [Xiaohongshu hall FAQ lookup](references/hall-faq-lookup.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown planning and confirmation cards, JSON command inputs, shell commands, and generated still image files when approved.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid lookup, generation, transform, and edit stages require explicit confirmation; terminal tasks report returned artifact details and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
