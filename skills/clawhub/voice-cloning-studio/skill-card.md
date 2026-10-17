## Description:

Helps users create a named, reusable personal or brand voice from an authorized speech sample and optionally hear a separately approved test reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to make a reusable voice from their own or an explicitly authorized speaker's recording for narration and brand content. They can review the price before cloning and request a separately priced test reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broad media-generation authority.

Mitigation: Connect only if that account access is acceptable; keep the device token private and disconnect when no longer needed.

Risk: Uploading a voice sample exposes sensitive voice data and can enable unauthorized cloning.

Mitigation: Use only your own voice or a speaker's explicitly authorized sample, and confirm consent before uploading.

Risk: Automatic updates can silently replace package files before later use.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if each replacement needs prior review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra skill homepage](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](references/consent-and-sample-readiness.md)
- [Clone execution and recovery](references/clone-and-proof-workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline commands and returned voice or audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the voice ID and actual task and billing details when returned; a test reading requires separate approval.]

## Skill Version(s):

0.2.5 (source: server-resolved release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
