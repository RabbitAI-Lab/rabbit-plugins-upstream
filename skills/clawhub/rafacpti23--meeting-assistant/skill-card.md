## Description:

AI Meeting Bot for Jitsi Meet & Google Meet via Habilis MCP Gateway (https://xvix.com.br). Joins calls, transcribes with diarization, interacts via duplex voice and generates structured minutes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rafacpti23](https://clawhub.ai/user/rafacpti23)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an AI agent join Jitsi Meet or Google Meet calls, transcribe live discussion with speaker identification, participate by voice when configured, and produce structured meeting minutes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can capture live meeting audio, chat, transcripts, and generated minutes.

Mitigation: Use it only in meetings where the operator has authority and participants have been notified or have given any required consent.

Risk: Meeting content and API credentials may be routed through a third-party gateway with limited disclosed controls.

Mitigation: Use restricted, revocable API keys with tight quotas; rotate any Gemini or OpenAI keys already shared through the gateway.

Risk: Confidential meeting use may be inappropriate without clear gateway handling terms.

Mitigation: Do not use it for confidential meetings unless credential handling, transcript retention, logging, subprocessors, and deletion controls are acceptable to the organization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rafacpti23/skills/meeting-assistant)
- [Habilis MCP Gateway](https://xvix.com.br)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell command examples, YAML configuration, text transcripts, and structured meeting minutes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Habilis, Gemini, and OpenAI API keys for the documented meeting workflows.]

## Skill Version(s):

1.0.1 (source: server release evidence; SKILL.md frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
