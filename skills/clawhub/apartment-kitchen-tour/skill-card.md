## Description:

Turn one kitchen photo the listing already uses into one short clip for the listing page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External property hosts, listing teams, and their agents use this skill to turn one existing kitchen listing photo into a short, single-shot kitchen clip. The workflow provides a free shot plan, checks current image-to-video constraints and price, waits for approval before paid generation, and reports the final clip details and charge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants and retains a shared local Beatra device token with broader account capabilities than the kitchen-video task needs.

Mitigation: Install only if that authorization is acceptable, keep the credential file private, use the documented uninstall flow to revoke access when appropriate, and disable automatic updates if desired.

Risk: Paid video generation can consume credits more than once if changed work is retried as recovery.

Mitigation: Require the production card and explicit approval before each paid animate call, use one opaque client request ID for recovery, and start changed prompts, photos, durations, or models as new approved work.

Risk: Generated motion can misrepresent a listing if it invents appliances, cabinet contents, text, or room features.

Mitigation: Inspect and transcribe the source photo, constrain motion to the documented vocabulary, require interior photos before opening fixtures, and report any output drift against the approved shot plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/apartment-kitchen-tour)
- [Beatra skill homepage](https://beatra.ai/skills/apartment-kitchen-tour)
- [Kitchen tour workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one approved Beatra image-to-video generation per kitchen photo and returns task, billing, and clip-review details.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
