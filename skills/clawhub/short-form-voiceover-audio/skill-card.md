## Description:

Generates ready-to-edit text-to-speech voiceover audio from approved short-video scripts, with voice selection, price estimate review, and factual handoff of returned task details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn final short-form video scripts into approved voiceover audio. It supports script preparation, voice and model selection, cost confirmation, paid synthesis, polling, and factual delivery of returned audio, duration, usage, and billing facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports broad shared Beatra account access through a device token.

Mitigation: Review before installing, authorize only if the access is acceptable, keep the token private, and revoke the device from Beatra Console or use the uninstall flow when finished.

Risk: The security evidence reports automatic package updates enabled by default.

Mitigation: Disable silent updates with `python3 scripts/mcp_client.py update --auto off` when review control is required, or run `python3 scripts/mcp_client.py update --check` before updating.

Risk: Voice synthesis is a paid operation, and duplicate submissions could create unintended work or charges.

Mitigation: Use one approved production card, one client request identity, and the documented task recovery flow instead of automatically resubmitting paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/short-form-voiceover-audio)
- [Beatra skill homepage](https://beatra.ai/skills/short-form-voiceover-audio)
- [Voiceover workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Installation registration](references/installation-registration.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON snippets and shell commands; returned task facts may include MP3 audio URLs and billing or usage fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before paid synthesis; normal handoff is MP3 voiceover audio with returned task metadata.]

## Skill Version(s):

0.1.8 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
