## Description:

Turn a coworking or daytime office brief into one office background music playlist of 8 to 15 low-stimulation instrumentals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, workspace operators, and agents use this skill to turn a daytime coworking, office, or cafe work-area brief into a labeled low-stimulation instrumental playlist plan. With approval, the skill guides Beatra music generation, polling, recovery, and delivery for each playlist slot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad Beatra device authorization, including wallet spend authority and non-music media scopes.

Mitigation: Review before installing and authorize only when that level of Beatra account access is acceptable; revoke or uninstall when the connection is no longer needed.

Risk: Music generation is billable and can create duplicate or unexpected charges if requests are replayed incorrectly.

Mitigation: Confirm the live model price, slot count, and one-request-per-slot plan before generation; reuse the same client_request_id only for byte-identical recovery.

Risk: The skill stores shared Beatra credentials and installation state under ~/.beatra.

Mitigation: Keep the credential file private, never expose tokens in chat or logs, and use the bundled uninstall workflow or Beatra Console revocation to disconnect.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with the documented update command when unattended package modification is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/coworking-day-pack)
- [Beatra skill homepage](https://beatra.ai/skills/coworking-day-pack)
- [Daytime playlist workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown playlist plan with Beatra generation command examples and task/result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans 8 to 15 instrumental tracks; generated results include returned task details, actual duration, artifacts when provided, and billing.net_charged_credits.]

## Skill Version(s):

0.1.1 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
