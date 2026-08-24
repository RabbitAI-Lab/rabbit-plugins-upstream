## Description:

Turn an article, notes, or a finished script into a listener-ready solo podcast episode with a consistent host voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, producers, and teams use this skill to adapt supplied articles, notes, outlines, newsletters, or approved scripts into solo podcast scripts and MP3 narration with a consistent host voice, pronunciation handling, pricing confirmation, and delivery records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared, persistent Beatra account token that may carry permissions and billing exposure beyond a single podcast-audio task.

Mitigation: Review Beatra account permissions and billing exposure before use, protect the stored ~/.beatra credential state, and use the documented disconnect or uninstall flow when the connection is no longer needed.

Risk: Automatic package updates are enabled by default and can change package files without a separate confirmation prompt.

Mitigation: Review the documented update behavior and disable automatic checks with the provided update command when controlled change management is required.

Risk: Paid synthesis requests can create charges, and careless retries after transport or authentication failures can duplicate work.

Mitigation: Require explicit approval before paid synthesis, preserve the same client_request_id for uncertain retries, and follow the documented billing and recovery flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/ai-podcast-voiceover)
- [Beatra skill homepage](https://beatra.ai/skills/ai-podcast-voiceover)
- [Episode script](references/episode-script.md)
- [Show profile](references/show-profile.md)
- [Voice, delivery, and recovery](references/voice-and-delivery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured task or audio-artifact metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include approved episode scripts, production confirmation cards, Beatra task identifiers, MP3 artifact details, usage, and billing facts.]

## Skill Version(s):

0.1.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
