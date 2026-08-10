## Description: <br>
Voice Agent Memory helps agents make and receive phone calls with real-time transcription, persistent BlueColumn memory storage, and caller-specific recall across calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to connect Twilio, ElevenLabs or Deepgram, BlueColumn memory, and Claude through a FastAPI bridge so a voice agent can recall prior caller context and store call transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Caller transcripts and recalled memory may contain sensitive personal or business information. <br>
Mitigation: Add caller notice and consent before recording, transcription, or memory storage, and define retention and deletion controls before deployment. <br>
Risk: Sensitive bridge endpoints can be exposed without effective authentication. <br>
Mitigation: Require real bearer-token validation on every sensitive endpoint before exposing the bridge to any network. <br>
Risk: Broad CORS and public tunnel exposure can increase unauthorized access risk. <br>
Mitigation: Restrict CORS to trusted origins and avoid public exposure until authentication and access controls are enforced. <br>
Risk: Broadly loaded environment files can expose high-value API credentials. <br>
Mitigation: Use scoped secrets for Twilio, voice, BlueColumn, and model-provider credentials instead of broadly loading shared .env files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/voice-agent-memory) <br>
- [Publisher profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Architecture overview](artifact/ARCHITECTURE.md) <br>
- [BlueColumn API endpoint](https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown documentation with Python and shell code examples; runtime bridge responses use JSON or server-sent events.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup instructions, API bridge code, test commands, and voice-agent response guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
