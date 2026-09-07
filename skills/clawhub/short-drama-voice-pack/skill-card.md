## Description:

Turn a vertical short-drama episode script into a labeled short drama voiceover pack with one consistent voice per role.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and agents use this skill to cast a vertical short-drama episode, synthesize each attributed speech block with a fixed role voice, and deliver labeled clips that can be placed in edit order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra bearer credential and requests broad media, wallet, task, artifact, and voice permissions.

Mitigation: Review the permission scope before installation, keep the credential out of chat, logs, command arguments, and environment variables, and reconnect only when the user explicitly authorizes it.

Risk: Automatic package-file updates are enabled by default and can replace package-owned files before ordinary commands.

Mitigation: For predictable reviewed code, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` before routine use.

Risk: Paid clone and speech generation calls can spend Beatra credits.

Mitigation: Confirm the voice cast, live estimate, and request IDs before paid calls, use one request identity per block, and retry uncertain paid work only with the identical frozen payload.

Risk: Voice cloning can create sensitive misuse risk if consent is not established.

Mitigation: Clone a role voice only after the user attests that the voice is theirs or that the speaker authorized the cloning use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/short-drama-voice-pack)
- [Short-drama voice-pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with labeled clip metadata, task status, billing fields, and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one Beatra synthesis task per approved speech block and reports returned artifact, duration, MIME type, resolved model, and net charged credits.]

## Skill Version(s):

0.1.2 (source: evidence.release, manifest.json, scripts)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
