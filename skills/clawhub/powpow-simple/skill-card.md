## Description:

Helps people publish travel stories and photos to PowPow and create chat-enabled digital humans on its public map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

PowPow account holders use this skill to draft and publish travel posts with optional photos and map locations, or to create public, chat-enabled digital humans. It also helps verify posts and remove the user's own test posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles PowPow login credentials and keeps a short-lived session token locally.

Mitigation: Only use it with an account you intend to connect; protect the local session and avoid sharing credentials in public conversations.

Risk: It can upload selected local images, publish public map posts, and delete the user's own posts without executable confirmation gates.

Mitigation: Review the content, images, location, and target post manually before running publication or deletion.

Risk: Creating a public digital human spends account badges.

Mitigation: Confirm the profile, map location, and badge cost before running creation.

## Reference(s):

- [PowPow Simple on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-simple)
- [PowPow](https://global.powpow.online)
- [Skill security and platform API notes](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown with commands and published-post links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include draft travel posts, publication status, and digital-human details.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
