## Description:

Turn three named new-item stills into a launch board you can post, then turn the rest of the set into a matching pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External store, cafe, retail, and chain-store teams use this skill to plan and generate fact-grounded new-item still sets, launch posters, and matching boards. It guides confirmation, billing, generation, review, delivery, and recovery for Beatra image-generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the package uses broad Beatra account access, credential handling, telemetry, and spending authority.

Mitigation: Install only when that access is acceptable, keep the shared Beatra credential private, avoid uploading sensitive local files, and review Beatra console or device access for shared credential use.

Risk: The security evidence says silent self-updates are enabled by default.

Mitigation: Use the documented update controls, including the `--auto off` command, when automatic updates are not acceptable for the installation.

Risk: The skill can submit billable image-generation tasks through Beatra.

Mitigation: Require the documented confirmation card before billable calls, read live model pricing before submission, and preserve request identity during recovery to avoid duplicate charges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/store-new-item-launch)
- [Beatra skill homepage](https://beatra.ai/skills/store-new-item-launch)
- [Store new-item workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON payloads and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces fact-based image generation plans, confirmation cards, request payload guidance, task recovery steps, and delivery checklists.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
