## Description:

Use Voiceover & Narration Studio as an AI voice generator, text-to-speech workspace, and AI voiceover generator for choosing voices, producing ready-to-edit narration, planning ordered long-form or multilingual speech, and creating authorized reusable brand voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to coordinate Beatra text-to-speech, voiceover, long-form narration, multilingual speech, and authorized voice cloning workflows. It helps plan approved paid requests, select current voices and models, estimate credit use, and return generated audio or reusable voice facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store a Beatra device credential locally.

Mitigation: Install only when the user trusts Beatra account access, keep the credential private, and use the documented uninstall or disconnect flow when access should be removed.

Risk: Approved speech synthesis or voice cloning can spend Beatra account credits.

Mitigation: Require a frozen production card, price estimate, and clear approval before each paid request; retry uncertain paid calls only with the same request identity and unchanged arguments.

Risk: Voice cloning can upload local voice samples.

Mitigation: Upload samples only after explicit confirmation that the speaker owns or authorized the voice, and do not imitate a voice without consent.

Risk: Installation registration can send package and environment metadata to Beatra.

Mitigation: Tell users that registration is non-blocking and account-scoped, and avoid treating registration failure as permission for additional voice work.

Risk: The bundled client can silently auto-update installed files during normal use.

Mitigation: Use the documented update controls to disable silent checks when desired, and rely on the package's checksum and rollback checks before accepting updates.

## Reference(s):

- [Voiceover & Narration Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Intent and routing](references/intent-and-routing.md)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Long-form and multilingual production](references/long-form-and-multilingual.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets, JSON request shapes, production cards, estimates, and returned task facts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe paid Beatra operations, local credential setup, sample upload, task polling, and generated audio or voice-clone result facts.]

## Skill Version(s):

0.1.7 (source: server release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
