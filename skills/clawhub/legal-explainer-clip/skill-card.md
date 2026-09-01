## Description:

Turn one public-education legal topic into a labeled digital-human still, a speakable explainer script, and one talking clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Law firms and firm marketing teams use this skill to turn a confirmed public-education legal topic into a reviewed still plan, short narration script, synthesized speech, and one labeled talking clip for marketing or educational channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a persistent shared Beatra device connection with broad media, artifact, task, and wallet-spending authority.

Mitigation: Install only with account approval, protect ~/.beatra/credentials.json as a sensitive token, and use the documented uninstall or revocation flow when removing the skill.

Risk: Silent automatic updates are enabled by default for the package installation.

Mitigation: Review the update setting immediately after installation; enterprises and regulated environments should disable silent updates or manage updates centrally.

Risk: Billable media generation can spend Beatra credits, and changed recovery arguments can create separate work.

Mitigation: Require staged user approval before each paid step, use one client_request_id per approved slot, and recover uncertain submissions only with unchanged arguments.

Risk: A legal explainer clip could be mistaken for case-specific legal advice or a real lawyer presentation.

Mitigation: Restrict use to public-education topics, refuse live matter details or win predictions, keep the non-lawyer presenter label readable, and require firm review before each production stage.

## Reference(s):

- [Legal explainer workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/legal-explainer-clip)
- [Beatra skill homepage](https://beatra.ai/skills/legal-explainer-clip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON payloads, and generated media artifact references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a still plan, speakable script, audio task, and talking clip only after staged user approvals.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
