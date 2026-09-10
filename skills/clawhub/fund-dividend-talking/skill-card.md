## Description:

Turn a user-supplied fund dividend announcement and authorized stills into one fund dividend talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and fund marketers use this skill to turn an already-supplied fund dividend announcement and authorized stills into short talking clips, while keeping spoken content limited to facts present in the announcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization stored under ~/.beatra.

Mitigation: Install only if this access is acceptable, keep the credential private, review Beatra account scopes, and revoke the device from the Beatra Console when no longer needed.

Risk: Selected local media may be uploaded to Beatra for asset, speech, or video workflows.

Mitigation: Use only authorized stills, voice samples, and announcement materials, and confirm likeness and voice rights before upload or generation.

Risk: Paid clone, speech, and video calls can spend Beatra credits.

Mitigation: Use the skill's live pricing cards, explicit per-stage confirmation, idempotent request IDs, and task polling before retrying or submitting changed work.

Risk: The bundled client silently checks for and applies package updates by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if silent replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/fund-dividend-talking)
- [Beatra skill homepage](https://beatra.ai/skills/fund-dividend-talking)
- [Dividend talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON and shell command snippets; generated media artifacts when Beatra tasks succeed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided announcement/stills and Beatra authorization; paid clone, speech, and video stages require explicit confirmation.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
