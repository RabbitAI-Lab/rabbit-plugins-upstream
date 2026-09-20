## Description:

Publishes PowPow travel posts and photo essays, creates map-pinned digital humans, and supports the related login, drafting, image, location, publishing, verification, and test cleanup workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to turn travel material, photos, or draft text into PowPow posts and to create digital humans on the public PowPow map. It guides the agent through account login, location selection, image handling, draft review, publishing, verification, and deletion of the user's own test posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or delete public PowPow content through the user's stored session.

Mitigation: Confirm the account, post content, images, location, and requested publish or delete action before running platform-changing commands.

Risk: Digital-human creation can spend account badges.

Mitigation: Confirm the badge cost and intended digital-human details before creation.

Risk: A short-lived stored session can continue to authorize account actions after setup.

Mitigation: Use the expected POWPOW_STATE_DIR and platformUrl, then clear the stored session after use when reducing the authorization window matters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/durenzidu/skills/powpow-integration)
- [PowPow Homepage](https://global.powpow.online)
- [PowPow Registration](https://global.powpow.online/register)
- [Security Architecture](references/security.md)
- [File Structure](references/file-structure.md)
- [Product Screenshots](references/screenshots.md)
- [Changelog](references/changelog.md)
- [PowPow Intro Video](https://www.bilibili.com/video/BV1Wu826UEVz/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [User-facing guidance with inline shell commands, Markdown links, and generated HTML draft files for PowPow posts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local draft HTML and manifest files before publishing; platform actions require the user's PowPow account session.]

## Skill Version(s):

2.1.14 (source: ClawHub release metadata; artifact frontmatter reports 5.7.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
