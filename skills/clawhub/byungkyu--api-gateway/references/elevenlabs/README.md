# ElevenLabs Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

> **⚠ Voice recordings are biometric data.** This app handles audio of real people speaking. A voice sample is a biometric identifier under GDPR Art. 9, BIPA, and similar laws — a stricter category than ordinary personal data — and the recordings themselves are usually private conversations: meetings, calls, voice notes, interviews, therapy or medical discussions.
>
> - **Voice cloning needs the speaker's consent, not just the user's.** Never create or fine-tune a voice from a recording unless the user confirms the person consented to a clone of their voice. A cloned voice can be used to impersonate them, including to defeat voice authentication and to fabricate statements they never made. Never clone a public figure or a voice taken from media the user does not own.
> - **Never upload audio the user did not name.** Speech-to-text and voice creation read a local file or URL and transmit it to ElevenLabs. Take the path from the user verbatim; do not search directories for audio, and do not upload a recording captured for some other purpose.
> - **Transcripts inherit the sensitivity of the conversation.** A meeting recording routinely contains third parties who never agreed to transcription, plus credentials, financials, and health details spoken aloud. Return the narrowest answer the task needs rather than printing whole transcripts, and do not forward them to another app or a trigger destination without explicit approval for that transfer.
> - **Generated speech is attributable to a person.** Confirm the exact text before synthesizing with a cloned or custom voice; the output sounds like a real human saying it.
> - Audio and voices persist in the user's ElevenLabs account until deleted, and generation consumes paid credits.

**App name:** `elevenlabs`
**Base URL proxied:** `api.elevenlabs.io`

## API Path Pattern

```
/elevenlabs/v1/{resource}
```

## Common Endpoints

### Text-to-Speech

#### Convert Text to Speech
```bash
POST /elevenlabs/v1/text-to-speech/{voice_id}
```

#### Stream Text to Speech
```bash
POST /elevenlabs/v1/text-to-speech/{voice_id}/stream
```

### Voices

#### List Voices
```bash
GET /elevenlabs/v1/voices
```

#### Get Voice
```bash
GET /elevenlabs/v1/voices/{voice_id}
```

#### Create Voice Clone
```bash
POST /elevenlabs/v1/voices/add
```

#### Delete Voice
```bash
DELETE /elevenlabs/v1/voices/{voice_id}
```

### Models

#### List Models
```bash
GET /elevenlabs/v1/models
```

### User

#### Get User Info
```bash
GET /elevenlabs/v1/user
```

#### Get Subscription Info
```bash
GET /elevenlabs/v1/user/subscription
```

### History

#### List History
```bash
GET /elevenlabs/v1/history?page_size=100
```

#### Get Audio from History
```bash
GET /elevenlabs/v1/history/{history_item_id}/audio
```

### Sound Effects

#### Generate Sound Effect
```bash
POST /elevenlabs/v1/sound-generation
```

### Audio Isolation

#### Remove Background Noise
```bash
POST /elevenlabs/v1/audio-isolation
```

### Speech-to-Text

#### Transcribe Audio
```bash
POST /elevenlabs/v1/speech-to-text
```

### Speech-to-Speech

#### Convert Voice
```bash
POST /elevenlabs/v1/speech-to-speech/{voice_id}
```

## Notes

- Text-to-Speech returns audio/mpeg data
- Sound Effects returns audio/mpeg data
- Cursor-based pagination with `page_size` and `start_after_history_item_id`
- Response headers include `x-character-count` for usage tracking
- Models available: `eleven_multilingual_v2`, `eleven_turbo_v2_5`

## Resources

- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference)
