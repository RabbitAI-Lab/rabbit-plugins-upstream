## Description:

Turn a user-supplied product factsheet and authorized stills into one wealth product talking clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External wealth advisors and hall educators use this skill to plan and create short talking clips that read only user-supplied wealth product factsheet points from authorized still images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device authorization can spend credits for generation tasks.

Mitigation: Review the Beatra account approval page before authorizing, require explicit approval for each paid clone, speech, and video stage, and use only user-selected files.

Risk: Silent automatic updates can replace package-owned files by default.

Mitigation: Consider disabling silent checks with `python3 scripts/mcp_client.py update --auto off`; updates should remain limited to verified Beatra discovery, CDN, manifest, archive, and file checks.

Risk: Generated wealth product speech could become misleading if the agent adds unsupported claims.

Mitigation: Speak only points already present in the supplied factsheet and do not invent yields, rankings, buy recommendations, price paths, or unstated terms.

Risk: Transport retries for paid generation could create duplicate or changed work.

Mitigation: Reuse the same opaque `client_request_id` only for byte-identical retry arguments; use a new request identity when the still, line, voice, duration, or other generation input changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/wealth-product-talking)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-product-talking)
- [Factsheet talking workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON payloads and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces labeled clip slot plans, approval cards, Beatra MCP command payloads, task status summaries, billing details, and generated media artifact metadata.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
