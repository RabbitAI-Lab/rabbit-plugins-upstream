## Description:

Turn public TikTok comments into one spoken reply clip per written line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External social media operators use this skill to turn public TikTok comments and prewritten replies into a reviewed list of spoken reply clips, then generate one audio file per approved reply through Beatra speech tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill grants and uses broad Beatra account authority that can spend credits and access broader Beatra media and task capabilities than this TikTok speech workflow needs.

Mitigation: Authorize only when that account-level access is acceptable, keep the Device Token private, review live production cards before billable calls, and revoke or disconnect the Beatra connection when it is no longer needed.

Risk: The security review says the bundled client silently self-updates executable code by default.

Mitigation: In managed or sensitive environments, disable automatic updates with `python3 scripts/mcp_client.py update --auto off` and review updates before enabling or applying them.

Risk: Billable lookup, clone, and speech requests can consume Beatra credits, and retries with changed inputs can create duplicate paid work.

Mitigation: Use live prices, one opaque `client_request_id` per approved request, poll existing tasks for recovery, and retry only byte-identical requests under the same identity.

Risk: Voice cloning may involve likeness rights and consent.

Mitigation: Use cloning only with an authorized sample, inspect the sample before upload, and require explicit confirmation before cloning or speech generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/tiktok-comment-reply-voice)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-comment-reply-voice)
- [TikTok comment reply workflow](artifact/references/workflow.md)
- [Comment lookup](artifact/references/comment-lookup.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with JSON and shell command blocks; task results may include MP3 audio artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one approved Beatra task per lookup, clone, or speech slot and reports task status, audio metadata, and net charged credits when available.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
