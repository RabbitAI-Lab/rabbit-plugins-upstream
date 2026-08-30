## Description:

Turns seller-supplied selling points into one Amazon A+ module still per point for Amazon A+ Content modules, selling-point modules, and brand-story graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and e-commerce creative teams use this skill to plan and generate one A+ page module still for each confirmed seller-supplied product benefit, with a clear free plan before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra device authorization that can spend credits and access multiple media tool families.

Mitigation: Review the Beatra approval scopes before installation and install only when that account-level access is acceptable.

Risk: Silent automatic updates are enabled by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when change control or review gates are required.

Risk: The skill uses shared local Beatra state and registration telemetry.

Mitigation: Avoid installing it in tightly controlled environments unless the shared `~/.beatra` state and registration behavior are acceptable.

## Reference(s):

- [A+ module workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/amazon-a-plus-module-pack)
- [Beatra skill homepage](https://beatra.ai/skills/amazon-a-plus-module-pack)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown plans and status messages with shell command examples; generated still images are returned as files or bytes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One paid image-generation task per approved module; reports task IDs, resolved models, dimensions, formats, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release metadata, artifact manifest, bundled scripts)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
