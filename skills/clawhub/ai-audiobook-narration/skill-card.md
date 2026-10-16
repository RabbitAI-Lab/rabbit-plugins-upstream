## Description:

Guides chapter-by-chapter audiobook production from final manuscript or course text using a consistent narrator, a representative pilot, and approved paid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, course creators, and their agents use this skill to plan and produce ordered audiobook chapters, confirm narrator and pronunciation choices with a pilot, and deliver audio with task and billing details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared local Beatra device token grants access to paid generation workflows.

Mitigation: Review the requested access before installation, protect the local credential, and explicitly approve each paid production step.

Risk: The skill silently updates its own package files by default.

Mitigation: Review update behavior before installation; disable automatic updates with the documented `update --auto off` command if you need to approve changes first.

Risk: Installation and runtime registration sends limited data to Beatra.

Mitigation: Review the documented registration data and privacy implications before connecting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/ai-audiobook-narration)
- [Beatra skill homepage](https://beatra.ai/skills/ai-audiobook-narration)
- [Chapter production](artifact/references/chapter-production.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Audio artifact links]

**Output Format:** [Markdown with chapter-ordered links and task details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pilot and subsequent chapters require separate approval for paid generation; reports actual task status, available audio artifacts, and billing facts.]

## Skill Version(s):

0.2.6 (source: server-resolved release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
