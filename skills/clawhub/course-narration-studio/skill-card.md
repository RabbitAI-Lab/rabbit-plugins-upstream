## Description:

Turns lesson materials into speakable scripts and slide-ready narration audio, organized by lesson in a consistent teacher voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Educators, trainers, and course creators use this skill to turn lesson manuscripts and slides into a reviewed, lecture-by-lecture narration pack with a consistent voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared full-scope Beatra device credential grants broad access across Beatra packages.

Mitigation: Review the requested access before authorizing, keep the credential private, and disconnect it when no longer needed.

Risk: The bundled client silently installs verified updates by default, changing package code without separate approval.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if changes require manual review.

Risk: Voice cloning and speech synthesis consume credits; repeated submissions can incur additional charges.

Mitigation: Confirm the voice, consent, and live cost estimates before paid requests; reuse the same request ID and unchanged arguments when recovering an uncertain submission.

## Reference(s):

- [Course Narration Studio release](https://clawhub.ai/beatra-ai/skills/course-narration-studio)
- [Course narration workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Audio files]

**Output Format:** [Lesson scripts and delivery notes in text or Markdown, with links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lesson audio is ordered and labeled with duration, usage, and charged credits.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
