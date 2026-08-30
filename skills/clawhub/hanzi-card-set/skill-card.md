## Description:

Turns user-supplied character lists into a four-to-eight still hanzi card set, with one still per confirmed character or named card group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and educators use this skill to plan and generate small hanzi recognition-card packs from characters and labels they already supplied. The workflow helps collect confirmed card lines, obtain approval before paid Beatra image generation, poll asynchronous tasks, and deliver returned artifacts with billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release requests broad Beatra device authorization and stores a bearer token under ~/.beatra.

Mitigation: Review the requested Beatra account permissions before use, keep the token out of chat, logs, command arguments, and environment variables, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: The bundled client performs silent automatic update checks and can update package-owned files by default.

Mitigation: Use scripts/mcp_client.py update --auto off when silent updates are not acceptable, and rely only on the documented update path that verifies discovery data, archive checksums, manifest checksums, and packaged file checksums.

Risk: Generation calls are paid Beatra tasks and retries can create billing ambiguity if request identity is changed.

Mitigation: Show the production card before the first billable call, use one opaque client_request_id per still, retry only byte-identical uncertain requests with the same ID, and report billing.net_charged_credits from terminal task results.

Risk: The skill sends installation metadata to Beatra during non-billable registration.

Mitigation: Treat registration as part of the Beatra connection posture and review that the package slug, version, platform, and stable installation reference are acceptable before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/hanzi-card-set)
- [Beatra skill homepage](https://beatra.ai/skills/hanzi-card-set)
- [Hanzi-card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with JSON payloads, inline shell commands, and returned image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a pack list and one planned still per confirmed character or group, capped at eight, with task IDs, resolved models, dimensions, formats, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server evidence release, manifest.json, bundled scripts)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
