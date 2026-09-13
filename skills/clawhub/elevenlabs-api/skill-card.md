## Description:

ElevenLabs API integration with managed authentication for text-to-speech, voice cloning, sound effects, and audio processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to access ElevenLabs through Maton-managed authentication for speech generation, voice cloning, sound effects, transcription, audio isolation, and related audio workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice recordings, cloned voices, transcripts, and generated speech can expose biometric or private conversation data and may enable impersonation.

Mitigation: Confirm speaker consent before cloning, use only user-named audio files, confirm exact generated text for cloned or custom voices, and return only the narrowest needed transcript or audio output.

Risk: Long-lived API keys and broad account connections can expose ElevenLabs or Maton access if mishandled.

Mitigation: Prefer OAuth, store credentials in the operating system credential store, avoid exporting MATON_API_KEY except when the CLI cannot be installed, and rotate any key that was printed, committed, or pasted.

Risk: Write, delete, generation, hosted function, and trigger operations can change account data, consume paid credits, or create persistent automation.

Mitigation: Require explicit approval for each connection, POST, PUT, PATCH, DELETE, deploy, invocation, trigger, or destination change; delete unused connections, hosted functions, and triggers when finished.

Risk: Trigger destinations can continuously forward event data to another host.

Mitigation: Prefer Maton-controlled destinations, never place credentials in destination headers or templates, and disclose the exact destination host, payload fields, and delivery persistence before approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/elevenlabs-api)
- [Maton Homepage](https://maton.ai)
- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference)
- [ElevenLabs Developer Portal](https://elevenlabs.io/developers)
- [ElevenLabs Models Overview](https://elevenlabs.io/docs/overview/models)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized ElevenLabs connection.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
