## Description:

Turn three named new-item stills into a launch board you can post, then turn the rest of the set into a matching pack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External store operators and agents use this skill to plan and generate a first three-still launch board, then complete a matching new-item image pack from confirmed store facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with broader authority than still-image generation.

Mitigation: Install only for accounts where the broader Beatra scopes and wallet-spend exposure are acceptable, and keep the credential private.

Risk: The bundled client can call remote Beatra tools and bill generation work through Beatra credits.

Mitigation: Review the six-field production card before paid work, require user approval before billable calls, and rely on live model and billing responses rather than remembered prices.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Disable automatic updates with the documented update command if separate review is required before package changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/store-new-item-launch)
- [Store new-item workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-generation plans, confirmation cards, Beatra tool-call commands, task polling guidance, and delivery summaries.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
