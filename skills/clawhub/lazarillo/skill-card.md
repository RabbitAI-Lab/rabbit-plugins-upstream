## Description:

Ojos y manos de una persona con baja vision: manda sus mensajes y sus notas de voz con confirmacion hablada obligatoria, le lee documentos y correo, y le redacta textos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kapitecsoluciones](https://clawhub.ai/user/kapitecsoluciones)

### License/Terms of Use:

MIT

## Use Case:

People with low vision use Lazarillo through a single chat to send confirmed WhatsApp messages or voice notes, hear useful document and email summaries, and draft text without having to search visually across an interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent has shell and messaging authority, so the skill should not be treated as a hard security boundary against a compromised or disobedient agent.

Mitigation: Grant the skill only when the operator accepts that authority, monitor messaging behavior, and place stronger enforcement in a separate process if hard guarantees are required.

Risk: Incorrect private contact, media, mode, or log configuration can cause failed sends, wrong routing, or weak auditability.

Mitigation: Configure the private data paths carefully, require full international phone numbers, test the channel before unattended use, and keep the audit copy outside the agent's writable area.

Risk: Some safeguards, including interruption handling and the no-send-on-silence rule, are described for the model to follow rather than enforced entirely in code.

Mitigation: Use supervised rollout, keep high-risk transactions out of scope, and validate operational behavior before relying on the skill for daily messaging.

Risk: Text messages are filtered for secrets and payment data, but forwarded voice notes are not inspected by the send script.

Mitigation: Do not use voice-note forwarding for passwords, payment details, one-time codes, or other sensitive content, and verify voice-note forwarding end to end before production use.

## Reference(s):

- [Montaje](references/montaje.md)
- [Modelo de amenaza](references/seguridad.md)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Spanish prose for voice playback, Markdown guidance, and shell command invocations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Messaging output is gated by spoken confirmation and records audit entries with content hashes rather than cleartext message bodies.]

## Skill Version(s):

0.2.0 (source: release evidence and CHANGELOG, released 2026-08-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
