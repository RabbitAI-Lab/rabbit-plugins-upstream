## Description:

Evolve Self-Improving helps an agent identify verified corrections, feature requests, knowledge gaps, and error lessons from the current conversation and maintain a scoped local knowledge and experience store for future reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzusp](https://clawhub.ai/user/zzusp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to preserve reusable, verified corrections, preferences, facts, and troubleshooting lessons across sessions while avoiding transient, speculative, or sensitive content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory can retain stale, overly broad, or sensitive details if entries are saved without enough review.

Mitigation: Review saved entries periodically, keep scopes narrow, and save only verified, desensitized facts or lessons; do not store credentials or unsanitized private content.

Risk: Incorrect or premature lessons can influence future agent behavior across sessions.

Mitigation: Require source confirmation, readback, conflict checks, and validation before adding or updating knowledge and experience entries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zzusp/skills/evolve-self-improving)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, generated index text, shell commands, and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes scoped local knowledge and experience entries under ~/.agent-knowledge/ only when evidence and validation gates pass.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
