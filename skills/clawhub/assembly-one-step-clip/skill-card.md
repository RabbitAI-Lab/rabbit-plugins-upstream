## Description:

Turn authorized stills and seller-supplied step facts into one assembly step video per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and listing teams use this skill to turn photographed assembly steps and seller-supplied step facts into one short video clip per still. It helps agents plan, price, submit, poll, and deliver paid Beatra image-to-video tasks without stitching multiple steps together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a persistent shared Beatra Device Token with spending authority and broader media capabilities than this assembly-video workflow requires.

Mitigation: Install only if that access is acceptable, keep the token private, review account activity and credit use, and avoid approving unexpected MCP tool calls outside the documented one-step assembly-video workflow.

Risk: Automatic updates are enabled by default and can replace package code without separate confirmation.

Mitigation: Use the documented `python3 scripts/mcp_client.py update --auto off` command before use when silent package replacement is not acceptable, and review update status with `python3 scripts/mcp_client.py update --check`.

Risk: Paid video generation can consume credits and duplicate submissions can create duplicate charges.

Mitigation: Require the six-field production card before submission, use one opaque `client_request_id` per still, and retry uncertain requests only with identical arguments and the same request identity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/assembly-one-step-clip)
- [Beatra skill homepage](https://beatra.ai/skills/assembly-one-step-clip)
- [Assembly one-step workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads; generated video artifacts are returned by Beatra tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One video task is created per admitted still, with task status, actual dimensions, duration, usage, and billing fields reported after completion.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
