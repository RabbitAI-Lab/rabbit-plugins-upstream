## Description:

Turn user-supplied drawing steps into one still per art demo page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, designers, and agents use this skill to turn confirmed classroom art lesson steps into planned page lists and generated art demonstration stills. It is intended for drawing step pages and art demo sets, with one still per approved step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared device token with broad media and wallet-related permissions.

Mitigation: Install only when that permission scope is acceptable, keep the token in the documented local credentials file, and revoke the connected agent from the Beatra Console when access is no longer needed.

Risk: Billable image generation can create unwanted charges if a request is repeated with changed inputs or without approval.

Mitigation: Use the skill's production-card confirmation step, one opaque request ID per approved step, and the documented same-ID recovery path for uncertain transport outcomes.

Risk: User-selected reference files may be uploaded to Beatra.

Mitigation: Upload only files the user explicitly supplies for the art demo and preserve their declared role without treating uploads as a source for missing lesson steps.

Risk: Silent automatic updates are enabled by default.

Mitigation: Use the documented update --auto off command when automatic replacement is not acceptable, and rely on the package's checksum and rollback controls for enabled updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/art-demo-set)
- [Beatra skill homepage](https://beatra.ai/skills/art-demo-set)
- [Art-demo workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown with inline shell and JSON payload examples; generated image artifacts are returned by remote tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled page list before billable work, then one generated still per approved step with task IDs, resolved models, dimensions, formats, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
