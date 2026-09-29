## Description:

Helps agents use an authenticated ElevenLabs connection to generate speech, clone voices, create sound effects, and process audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other ElevenLabs users can guide an agent to list voices, generate speech or sound effects, clone voices, and process audio through their connected account. Optional hosted functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice clones, uploaded audio, and generated speech may expose sensitive content or consume paid credits.

Mitigation: Review the content, voice, files, and expected charges before approving each action.

Risk: Connecting an account grants access within the connection's authorization.

Mitigation: Approve connections explicitly and limit their access to the task at hand.

Risk: Hosted functions, triggers, and destinations can automate actions or forward events persistently.

Mitigation: Review and approve each function, trigger, destination, and recipient before enabling automation.

## Reference(s):

- [ClawHub ElevenLabs skill](https://clawhub.ai/byungkyu/skills/elevenlabs-api)
- [Maton](https://maton.ai)
- [ElevenLabs API reference](https://elevenlabs.io/docs/api-reference)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may generate or process audio in the connected ElevenLabs account; the agent's output is primarily text and code.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
