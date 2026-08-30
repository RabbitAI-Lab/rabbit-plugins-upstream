## Description:

Turn a named product launch into three visual-tone stills, then one opening film clip for the stage screen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External brand and marketing teams use this skill to plan a three-frame launch tone board and produce a short stage-screen opening film for a named product, brand, or launch event.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Beatra device authorization is broader than this single image/video workflow.

Mitigation: Install only if that authorization scope is acceptable, keep the credential private, and revoke the Beatra device authorization when the skill is no longer used.

Risk: Automatic package updates are enabled by default and can replace package-owned code without a separate prompt.

Mitigation: In controlled or enterprise environments, run scripts/mcp_client.py update --auto off after installation; if updates remain enabled, rely on the documented checksum and fixed-source verification controls.

Risk: Paid media generation can create duplicate or unintended charges if uncertain requests are resubmitted with changed inputs.

Mitigation: Use one opaque client_request_id per approved request, retry only byte-identical uncertain requests with the same ID, and require a fresh production card for changed work.

## Reference(s):

- [Product launch opening-film workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/product-launch-opening-film)
- [Beatra skill homepage](https://beatra.ai/skills/product-launch-opening-film)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown production cards, command examples, task status summaries, and generated media artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans three stills before billable media generation, then produces one 2-15 second opening film clip.]

## Skill Version(s):

0.1.1 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
