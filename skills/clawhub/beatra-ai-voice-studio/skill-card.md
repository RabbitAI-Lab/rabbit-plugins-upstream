## Description:

Use Beatra AI Voice Studio as an AI voice generator, text-to-speech workspace, and AI voiceover generator. Choose from the current voice library, turn scripts into ready-to-edit AI narration and voiceover, or create and reuse a custom brand voice through voice cloning. It supports short-video voiceover, script-to-voiceover, course narration, ordered audiobook narration, supplied multilingual text to speech, Cantonese text to speech, and recurring brand audio, with current price estimates, clear output planning, and delivery organized by chapter, language, and use case.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, teams, and agents use this skill to plan and run Beatra voice generation work from supplied or approved text, including text-to-speech narration, short voiceovers, long-form audio, supplied multilingual speech, and authorized voice cloning. It guides voice selection, live model and price checks, approval boundaries, paid request submission, task recovery, and result reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Beatra credits for approved voice synthesis or voice cloning work.

Mitigation: Review the production card before paid work and approve only the exact text, sample, model, voice, estimate, and request count intended.

Risk: The Beatra authorization grants broader account powers than voice work alone may require.

Mitigation: Review the Beatra authorization page before connecting and revoke the device authorization from the console when the skill is no longer needed.

Risk: Voice cloning can upload local voice samples and create reusable voices.

Mitigation: Upload samples only after explicit speaker consent and keep clone approval separate from any later speech synthesis request.

Risk: A bearer token is stored locally under ~/.beatra.

Mitigation: Keep the credential file private, avoid sharing token contents in prompts or logs, and use the uninstall or console revocation path when access should end.

Risk: The bundled client can silently replace package files through automatic updates.

Mitigation: Disable automatic updates for reviewed or controlled environments and use manual update checks before accepting a newer package.

## Reference(s):

- [Beatra AI Voice Studio ClawHub page](https://clawhub.ai/beatra-ai/skills/beatra-ai-voice-studio)
- [Beatra AI Voice Studio homepage](https://beatra.ai/skills/beatra-ai-voice-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Long-form and multilingual production](references/long-form-and-multilingual.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report Beatra task, billing, voice, model, and audio artifact facts returned by the service.]

## Skill Version(s):

0.2.6 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
