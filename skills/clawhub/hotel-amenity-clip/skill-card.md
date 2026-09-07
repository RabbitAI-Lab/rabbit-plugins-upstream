## Description:

Turns labeled hotel amenity stills into one short Beatra-generated video clip per still after planning, model checks, and production approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External hotel sellers and hosts use this skill to turn existing labeled amenity photos into one short facility video per still. It produces a free shot list before any billable Beatra animation call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra Device Token can authorize more than hotel amenity video generation.

Mitigation: Install only when the publisher is trusted, keep the token in the private ~/.beatra credential file, and revoke or uninstall through the bundled workflow when access is no longer needed.

Risk: The bundled client silently checks for and installs verified package updates before ordinary Beatra commands.

Mitigation: Review before installing and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a pinned local package is required.

Risk: Local amenity images are uploaded to Beatra and Beatra credits may be spent after production approval.

Mitigation: Use the free shot list first, require explicit approval before animation, read current model pricing and balance, and submit each paid request once with a unique client_request_id.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/hotel-amenity-clip)
- [Beatra Skill Homepage](https://beatra.ai/skills/hotel-amenity-clip)
- [Hotel amenity clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples, shell commands, and returned Beatra task and artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce one video artifact per labeled amenity still after explicit paid production approval.]

## Skill Version(s):

0.1.2 (source: server release evidence, manifest, bundled scripts)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
