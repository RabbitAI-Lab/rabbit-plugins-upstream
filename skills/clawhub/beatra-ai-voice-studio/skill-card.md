## Description:

Use Beatra AI Voice Studio as an AI voice generator, text-to-speech workspace, and AI voiceover generator. Choose from the current voice library, turn scripts into ready-to-edit AI narration and voiceover, or create and reuse a custom brand voice through voice cloning. It supports short-video voiceover, script-to-voiceover, course narration, ordered audiobook narration, supplied multilingual text to speech, Cantonese text to speech, and recurring brand audio, with current price estimates, clear output planning, and delivery organized by chapter, language, and use case.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and run Beatra voice workflows, including voice selection, text-to-speech narration, ordered long-form or multilingual productions, and authorized voice cloning. It helps the agent prepare approval cards, call Beatra MCP tools, track billable requests, and return generated audio or reusable voice facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra bearer token stored locally.

Mitigation: Install only when the user trusts Beatra's account and MCP service; keep the token out of chat, logs, command arguments, and environment variables, and use the bundled uninstall flow when disconnecting.

Risk: The installed package sends non-secret installation metadata to Beatra.

Mitigation: Treat installation registration as part of the connection posture and avoid using the skill where package, version, platform, and installation reference telemetry is unacceptable.

Risk: Silent package updates are enabled by default.

Mitigation: Trust the Beatra CDN and update channel before installation, or disable automatic updates with the documented update command after installation.

Risk: Text-to-speech and voice-cloning calls are billable and can create asynchronous tasks.

Mitigation: Use explicit production approval, one client request identity per paid request, and recovery checks before retrying so uncertain delivery does not create duplicate paid work.

Risk: Voice cloning can misuse a speaker's voice if consent is missing.

Mitigation: Confirm that the sample is the user's own voice or that the speaker explicitly authorized cloning before any upload or clone request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/beatra-ai-voice-studio)
- [Beatra AI Voice Studio homepage](https://beatra.ai/skills/beatra-ai-voice-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Long-form and multilingual production](references/long-form-and-multilingual.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference Beatra task IDs, generated audio artifact URLs, billing facts, and cloned voice IDs returned by the service.]

## Skill Version(s):

0.2.5 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
