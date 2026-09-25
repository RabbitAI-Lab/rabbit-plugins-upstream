## Description:

Helps users publish photo-based travel posts to PowPow and create digital humans pinned to its public map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow account holders use this skill to turn photos and travel notes into published posts, or create digital humans on the public map. It also helps prepare drafts, locate places, upload images, and verify publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and the saved session token can grant access to a PowPow account.

Mitigation: Treat the password prompt as sensitive and keep POWPOW_STATE_DIR private.

Risk: Publishing posts or creating digital humans changes the user's account and may make content public.

Mitigation: Review each draft and digital-human creation carefully before approving publication.

Risk: A custom platform URL could send account activity to an untrusted server.

Mitigation: Do not override platformUrl unless the destination is fully trusted.

## Reference(s):

- [PowPow Classic on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-integration)
- [PowPow website](https://global.powpow.online)
- [Skill changelog](artifact/references/changelog.md)
- [Skill usage guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text and Markdown with draft posts, commands, and publication links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can publish posts and digital humans to a public map after user review.]

## Skill Version(s):

2.1.15 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
