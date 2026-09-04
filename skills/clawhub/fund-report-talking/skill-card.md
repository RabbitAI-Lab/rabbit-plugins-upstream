## Description:

Turn a user-supplied fund quarterly report highlight sheet and authorized stills into one fund quarterly report talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and fund marketers use this skill to create short, factual talking clips from already-supplied quarterly fund report highlights and authorized still images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests a shared Beatra Device Token with broad tool and wallet-spending authority.

Mitigation: Review Beatra account and device permissions before authorizing, keep the token in the documented credential file only, and revoke the device from Beatra Console when access is no longer needed.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` after install if manual review is required before package changes.

Risk: Paid clone, speech, and video requests can spend wallet credits.

Mitigation: Use the skill's per-stage confirmation cards, live pricing checks, opaque request IDs, and task polling before creating or retrying paid requests.

## Reference(s):

- [Quarterly report talking workflow](artifact/references/workflow.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)
- [Beatra skill homepage](https://beatra.ai/skills/fund-report-talking)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/fund-report-talking)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 2-8 separate talking clips and may drive Beatra clone, speech, upload, video, task, and billing operations through the bundled client.]

## Skill Version(s):

0.1.1 (source: evidence.json release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
