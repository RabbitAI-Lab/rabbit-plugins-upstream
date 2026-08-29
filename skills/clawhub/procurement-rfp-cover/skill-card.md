## Description:

Turn seller-supplied tender facts into one RFP cover still per project. This tender cover studio lays out the seller-supplied project title and agency lines as a bidding-document cover and RFP cover graphic. Use it for tender document covers, bid-file covers, and RFP cover stills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and proposal teams use this skill to turn confirmed project and agency details into individual RFP or tender cover stills. The agent plans the cover list, confirms billable Beatra image generation, submits one project per task, and reports returned files, task metadata, dimensions, formats, models, and net charged credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, seller-provided tender facts, and optional uploaded reference files may be sent to Beatra for generation.

Mitigation: Use only confirmed facts that the seller is permitted to share, avoid unnecessary sensitive content, and consider a dedicated Beatra account or workspace.

Risk: The bundled client stores a persistent Beatra bearer token locally and uses broad account permissions.

Mitigation: Review local credential controls before installation, protect the user's Beatra credential files, and reconnect or use a dedicated account if the permission scope is not acceptable.

Risk: Silent automatic updates are enabled by default.

Mitigation: In sensitive environments, disable automatic updates with the documented `python3 scripts/mcp_client.py update --auto off` command and perform reviewed updates explicitly.

Risk: Image generation is billable after user confirmation, and estimates may differ from settled usage.

Mitigation: Read live model pricing, show the six-field production card before paid calls, submit with idempotent request IDs, and report `billing.net_charged_credits` from terminal task results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/procurement-rfp-cover)
- [Beatra package homepage](https://beatra.ai/skills/procurement-rfp-cover)
- [RFP cover workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, files]

**Output Format:** [Markdown guidance plus generated image files and task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One RFP cover still per named project, normally 4 to 8 stills, with observed dimensions, formats, task IDs, resolved models, and billing.net_charged_credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
