## Description:

Creates an authorized reusable voice clone for recurring podcast, course, creator series, or brand narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, podcast teams, course producers, and brand teams use this skill to create a consented reusable voice and generate recurring narration in that same voice. The workflow covers consent checks, paid clone admission, episode synthesis, billing recovery, and delivery of labeled audio outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device credential with powers beyond voice generation.

Mitigation: Install only when the user accepts the broader Beatra authorization, keep the credential in the documented private local file, and avoid exposing tokens in conversation, logs, commands, or diffs.

Risk: Voice cloning can misuse a speaker's identity if consent is missing or assumed from file access.

Mitigation: Require explicit consent that the user owns the voice or has authorization before clone creation, and treat any changed sample, display name, or clone model as new clone work.

Risk: Clone and synthesis requests consume Beatra credits and transport uncertainty can create duplicate paid work.

Mitigation: Show the live estimate before paid submission, use one stable client_request_id per logical request, poll existing tasks before retrying, and retry only unchanged payloads after recovery.

Risk: Silent package self-updates are enabled by default.

Mitigation: Review the documented update behavior and disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when a pinned local package is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/voice-clone-series-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/voice-clone-series-studio)
- [Series Voice Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing workflow steps for Beatra voice clone, text-to-speech, task polling, billing, recovery, update, and uninstall operations.]

## Skill Version(s):

0.1.3 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
