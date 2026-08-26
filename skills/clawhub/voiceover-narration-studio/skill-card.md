## Description:

Use Voiceover & Narration Studio as an AI voice generator, text-to-speech workspace, and AI voiceover generator. Choose from the current voice library, turn scripts into ready-to-edit AI narration and voiceover, or create and reuse a custom brand voice through voice cloning. It supports short-video voiceover, script-to-voiceover, course narration, ordered audiobook narration, supplied multilingual text to speech, Cantonese text to speech, and recurring brand audio, with current price estimates, clear output planning, and delivery organized by chapter, language, and use case.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and production teams use this skill to plan and submit Beatra text-to-speech, long-form narration, multilingual narration, and authorized voice-cloning work. It helps choose current voices and models, estimate paid requests, preserve approvals, and deliver returned audio facts or reusable voice IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra account authorization, including wallet-spend and non-voice media scopes.

Mitigation: Install only after reviewing the requested access; keep the Device Token private, use the bundled authorization flow, and revoke or uninstall the connection when it is no longer needed.

Risk: Automatic updates are silent by default and can replace installed package files.

Mitigation: Use the documented update controls to disable silent checks or run an explicit update check, and rely on the package's checksum and channel verification before replacement.

Risk: Voice samples and cloned voices are sensitive and can enable impersonation if used without consent.

Mitigation: Require an explicit statement that the sample is the user's own voice or that the speaker authorized cloning before uploading or submitting a clone request.

Risk: Paid synthesis or cloning requests can create charges or duplicate work if retried incorrectly.

Mitigation: Freeze the approved request card first, submit each billable request once with one request identity, and retry only the exact same request when task creation is genuinely uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Beatra skill homepage](https://beatra.ai/skills/voiceover-narration-studio)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Voice casting and delivery](artifact/references/voice-casting-and-delivery.md)
- [Voice cloning and review](artifact/references/voice-cloning-and-review.md)
- [Long-form and multilingual production](artifact/references/long-form-and-multilingual.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [MCP connection](artifact/references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, text]

**Output Format:** [Markdown guidance with JSON snippets and shell commands; successful tasks return audio metadata, task facts, billing facts when present, or reusable voice IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces ready-to-edit speech audio facts or reusable voice IDs. It does not claim video, lip-sync, transcription, waveform editing, publication, refunds, or audio listening unless returned facts support them.]

## Skill Version(s):

0.1.5 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
