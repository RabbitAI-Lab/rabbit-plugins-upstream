## Description:

Turn a written incident briefing script into one incident brief voice clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Safety and operations teams use this skill to turn an already-written incident briefing script into a labeled set of short voice clips. It helps the agent plan the clip list, confirm paid speech or voice-clone work, submit Beatra MCP calls, and report task, billing, and audio-result details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra Device Token grants broad account authority, including speech generation, voice operations, uploads, wallet spend, task reads, artifact reads, and task cancellation.

Mitigation: Install only when that account access is acceptable, keep the token in the documented local credential file, review account permissions and billing exposure before sensitive use, and use the uninstall or console revocation path when disconnecting.

Risk: Automatic package updates are enabled by default and can replace package-owned files without a separate confirmation.

Mitigation: For sensitive environments, disable silent updates with the documented update command before use and review package changes before re-enabling automatic updates.

Risk: Paid clone or speech requests can consume credits, and retrying an uncertain request with changed arguments can create duplicate work or charges.

Mitigation: Use live model and price cards, confirm each paid stage, assign one opaque client_request_id per logical request, and retry only byte-identical uncertain submissions with the same request identity.

Risk: Voice cloning can misuse a staff likeness if file access is treated as consent.

Mitigation: Use cloning only when the requester provides rights for the sample, inspect the authorized sample first, and keep clone and speech approvals as separate paid stages.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/incident-brief-voice)
- [Beatra Skill Homepage](https://beatra.ai/skills/incident-brief-voice)
- [Incident Brief Voice Workflow](references/workflow.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Installation Registration](references/installation-registration.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [MCP Connection](references/mcp-connection.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with labeled lists, JSON payload examples, shell commands, and audio artifact references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a planned list of 8 to 20 voice-clip slots before paid work; after approval, it may create MP3 speech clips through Beatra and report task metadata, audio properties, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
