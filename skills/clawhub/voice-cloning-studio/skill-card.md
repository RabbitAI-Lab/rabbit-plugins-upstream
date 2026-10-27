## Description:

Creates a reusable personal or brand voice from an authorized speech sample and can produce an optional short test reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams can use the skill to make a reusable voice from their own or an authorized speaker's clean sample, then use that voice for narration and brand content. An optional test reading is a separate paid operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authorization includes paid image, video, and music generation beyond this skill's voice-cloning purpose.

Mitigation: Review the complete authorization scope before connecting, and revoke access through the Beatra Console when it is no longer needed.

Risk: Voice samples are subject to Beatra's processing and retention practices, and installation analytics are collected.

Mitigation: Review Beatra's voice-data processing, retention, and analytics terms before uploading a sample.

Risk: If the local skill inventory is corrupted, uninstalling may disconnect other Beatra skills.

Mitigation: Check the shared connection's other installed Beatra skills before uninstalling; device access can also be revoked through the Beatra Console.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra skill page](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](artifact/references/consent-and-sample-readiness.md)
- [Clone execution and recovery](artifact/references/clone-and-proof-workflow.md)
- [Test-reading review and voice reuse](artifact/references/review-recovery-and-voice-reuse.md)
- [Updates and security](artifact/references/updates-and-security.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Audio, Guidance, JSON]

**Output Format:** [A reusable voice asset, optional short test-reading audio, and concise text with structured task results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A test reading is separate paid work and requires its own approval.]

## Skill Version(s):

0.3.1 (source: server-resolved release evidence, manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
