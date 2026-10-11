## Description:

Guides an agent in turning one pet photo and a short script or approved voice clip into a shareable talking-pet video, with checks for pet identity, speech, and mouth synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and content creators use this skill to make greetings, reactions, stories, and other short talking-pet clips from a clear photo and approved speech or a short script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected pet media and generated outputs are sent to Beatra.

Mitigation: Inspect media and obtain permission before upload; avoid sharing sensitive or unapproved content.

Risk: One locally stored Beatra Device Token is shared across Beatra skills.

Mitigation: Keep the credential private with user-only file permissions; use the documented disconnect process when removing the last Beatra skill.

Risk: Speech and video generation can consume paid credits.

Mitigation: Show estimates and obtain the documented separate approvals before each billable stage; check available credits first.

Risk: Installed package code updates silently by default.

Mitigation: Review the update policy and disable automatic updates with the documented control if approval before code changes is required.

## Reference(s):

- [Talking Pet Video on ClawHub](https://clawhub.ai/beatra-ai/skills/talking-pet-video)
- [Talking Pet Video product page](https://beatra.ai/skills/talking-pet-video)
- [Talking-pet workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Video artifact references]

**Output Format:** [Markdown guidance with commands and links to generated audio and video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned by Beatra after asynchronous tasks complete; review quality and actual billing before delivery.]

## Skill Version(s):

0.2.1 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
