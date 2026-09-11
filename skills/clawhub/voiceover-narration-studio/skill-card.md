## Description:

Use Voiceover & Narration Studio as an AI voice generator, text-to-speech workspace, and AI voiceover generator. Choose from the current voice library, turn scripts into ready-to-edit AI narration and voiceover, or create and reuse a custom brand voice through voice cloning. It supports short-video voiceover, script-to-voiceover, course narration, ordered audiobook narration, supplied multilingual text to speech, Cantonese text to speech, and recurring brand audio, with current price estimates, clear output planning, and delivery organized by chapter, language, and use case.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to plan and generate ready-to-edit speech audio from approved text, coordinate long-form or multilingual narration, and create authorized reusable voice clones.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with permissions beyond voice generation.

Mitigation: Review the OAuth approval scopes before authorizing and revoke the device from the Beatra Console if the connection should no longer be trusted.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when local review is required before code changes.

Risk: Voice samples, approved scripts, and generated content are sent to Beatra for remote processing.

Mitigation: Upload voice samples only after explicit speaker authorization and treat submitted text and media as data shared with Beatra.

Risk: Speech synthesis and voice cloning are billable operations.

Mitigation: Require an approved production card, create one client request identity per paid request, and poll the returned task instead of submitting replacements.

## Reference(s):

- [ClawHub Release Page](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/voiceover-narration-studio)
- [Intent and Routing](references/intent-and-routing.md)
- [Voice Casting and Delivery](references/voice-casting-and-delivery.md)
- [Long-form and Multilingual Production](references/long-form-and-multilingual.md)
- [Voice Cloning and Review](references/voice-cloning-and-review.md)
- [Billing, Errors, and Recovery](references/billing-errors-and-recovery.md)
- [Installation and Authentication](references/installation-and-auth.md)
- [Automatic Updates and Safety](references/automatic-updates-and-safety.md)
- [MCP Connection](references/mcp-connection.md)
- [Tasks and Results](references/tasks-and-results.md)
- [Uninstall and Disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON MCP call payloads and shell command snippets; successful tasks report returned Beatra artifact, voice, usage, billing, and task facts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid synthesis and cloning calls require approved production cards; outputs may include Beatra audio artifact URLs or cloned voice IDs when returned by the service.]

## Skill Version(s):

0.1.8 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
