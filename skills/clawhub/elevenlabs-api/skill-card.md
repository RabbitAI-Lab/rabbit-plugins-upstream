## Description:

ElevenLabs API integration with managed authentication for text-to-speech, voice cloning, sound effects, and audio processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to access an authorized ElevenLabs account through Maton for generating speech, cloning or managing voices, processing audio, and building approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or modify ElevenLabs account resources through an authorized Maton connection.

Mitigation: Use OAuth when possible, confirm connection creation, and approve each write or upload only after reviewing the target resource and payload.

Risk: Voice samples, cloned voices, and transcripts can expose sensitive biometric or conversational data.

Mitigation: Use only user-named audio files, require confirmation that the speaker consented to voice cloning, and return only the minimum transcript or audio information needed for the task.

Risk: Hosted functions and triggers can create persistent automation or data egress.

Mitigation: Deploy only user-reviewed handlers, prefer DENY_ALL network policy, and get separate approval for each trigger destination, payload, and delivery pattern.

Risk: Long-lived API keys can be exposed through environment variables or logs.

Mitigation: Prefer OAuth and operating-system credential storage; use raw HTTP with MATON_API_KEY only when the CLI is unavailable and avoid logging credentials or full raw responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/elevenlabs-api)
- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference)
- [ElevenLabs Developer Portal](https://elevenlabs.io/developers)
- [ElevenLabs Models Overview](https://elevenlabs.io/docs/overview/models)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call authenticated Maton APIs and should minimize returned sensitive audio, voice, and transcript data.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
