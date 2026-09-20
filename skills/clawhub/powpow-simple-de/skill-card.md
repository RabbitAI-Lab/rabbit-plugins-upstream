## Description:

Publishes travel posts and stories to PowPow and creates chat-capable Digital Humans pinned to the public map, using a PowPow account for login, image upload, geocoding, publishing, verification, and user-owned test cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users use this skill to turn photos or raw travel material into public PowPow map posts, and to create Digital Humans at chosen locations. The workflow also supports login, self-checks, place lookup, image handling, post verification, and deletion of the authenticated user's own test posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles PowPow login credentials and stores a temporary PowPow session token on disk.

Mitigation: Use only when comfortable granting the agent PowPow account access, consider a dedicated PowPow account, and delete the session file after use when appropriate.

Risk: The skill can publish posts, create Digital Humans that spend badges, and delete the authenticated user's own posts without script-enforced confirmation.

Mitigation: Review the exact post, images, location, account, badge cost, and deletion target before any publish, create, or delete step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-simple-de)
- [PowPow homepage](https://global.powpow.online)
- [PowPow map](https://global.powpow.online/map)
- [Security architecture and platform API](references/security.md)
- [Changelog](references/changelog.md)
- [File structure](references/file-structure.md)
- [Product screenshots](references/screenshots.md)
- [Chinese edition](https://clawhub.ai/durenzidu/skills/powpow-simple)
- [English edition](https://clawhub.ai/durenzidu/skills/powpow-simple-en)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated draft files for PowPow publishing workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, a PowPow account, and optional POWPOW_STATE_DIR, POWPOW_PASSWORD, and UNSPLASH_ACCESS_KEY environment variables.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter, config, and changelog list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
