## Description:

Creates and reviews a short singing video from one portrait and a singing-audio excerpt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators use the skill to turn a portrait and a chosen singing excerpt into a short clip for greetings, playful posts, character art, or song promotion. It reviews the returned clip for facial movement, performance, audio presence, and synchronization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared authorization includes spending and voice-management permissions beyond the portrait-video task, and the client does not enforce a portrait-only boundary.

Mitigation: Review the requested authorization before installing and revoke the device through Beatra's Console when access is no longer wanted.

Risk: Selected media is sent to Beatra, and installation analytics are sent automatically.

Mitigation: Use only media you are authorized to share and account for the automatic analytics before installation.

Risk: Video generation can incur charges.

Mitigation: Require the user's confirmation before paid generation, as described in the skill instructions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/photo-singing-video)
- [Singing-photo workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Updates and security](references/updates-and-security.md)
- [Installation and authentication](references/installation-and-auth.md)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [A generated singing-video artifact or link with a concise task and output review.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One portrait and one singing-audio excerpt per video run; reports only task and billing details actually returned.]

## Skill Version(s):

0.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
