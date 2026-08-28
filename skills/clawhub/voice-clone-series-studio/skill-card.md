## Description:

Clone one voice you own and keep using it for a series of episodes, updates, and lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and teams use this skill to create an authorized reusable voice clone and generate recurring podcast, course, creator series, or brand-update narration in that same voice. It guides consent checks, paid clone admission, episode synthesis, task polling, billing review, and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can misuse a person's voice or an unauthorized brand voice.

Mitigation: Require explicit user attestation that the voice is their own or authorized, and treat file access alone as insufficient consent.

Risk: The bundled client uses a broad Beatra device token for speech, voice, wallet, task, artifact, and cancellation operations.

Mitigation: Keep the token only in the private Beatra credential file, avoid printing or moving it into chat, logs, arguments, or environment variables, and revoke access during uninstall when requested.

Risk: Voice clone and speech synthesis operations consume paid Beatra credits and may create duplicate charges if retried incorrectly.

Mitigation: Show live pricing before paid work, require confirmation, use stable client request IDs, poll existing tasks, and retry only unchanged requests when transport delivery is uncertain.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Consider disabling automatic updates with `python3 scripts/mcp_client.py update --auto off`; when enabled, rely on the bundled checksum and package ownership checks before replacement.

Risk: The skill sends voice samples, scripts, package metadata, and platform registration data to Beatra services.

Mitigation: Use only with content the user is comfortable submitting to Beatra and avoid exposing sensitive prompts, tokens, or private input content in recovery explanations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/voice-clone-series-studio)
- [Beatra skill homepage](https://beatra.ai/skills/voice-clone-series-studio)
- [Series voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides Beatra voice-clone and text-to-speech tasks that can return audio artifacts, task status, usage, and billing fields.]

## Skill Version(s):

0.1.2 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
