## Description:

Turn a written customer-onboarding step list into one customer onboard voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Enablement and customer success teams use this skill to turn an existing customer-onboarding step list into a labeled pack of spoken onboarding clips. It plans the clip slots, handles voice selection or authorized voice cloning, submits paid Beatra speech tasks, and reports returned audio artifacts and billing results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill links a Beatra account and stores a reusable device token in ~/.beatra.

Mitigation: Review the Beatra approval scopes before authorizing and uninstall or disconnect the package when the account connection is no longer needed.

Risk: The authorization grants broad Beatra account powers beyond a narrow voice-only credential.

Mitigation: Install only when the requested media, task, artifact, wallet, and voice scopes match the intended workflow.

Risk: The skill can submit paid remote voice clone and speech operations.

Mitigation: Require the documented approval cards before paid stages, use opaque client request IDs, and do not retry billable work unless recovery rules allow the same unchanged request identity.

Risk: Silent package updates are enabled by default.

Mitigation: Use the documented update command to disable automatic updates when manual review of package changes is required.

## Reference(s):

- [Customer onboard voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/cs-onboard-voice)
- [Beatra skill homepage](https://beatra.ai/skills/cs-onboard-voice)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and returned audio artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled 8 to 20 clip plan before paid work and may return generated MP3 voice clip artifacts after Beatra tasks complete.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
