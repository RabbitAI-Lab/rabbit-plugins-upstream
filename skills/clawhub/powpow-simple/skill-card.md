## Description:

Publishes travel posts or photo journals to PowPow and creates map-pinned digital humans for PowPow accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users and OpenClaw agents use this skill to turn photos, text, or trip notes into PowPow posts, resolve locations and images, and create digital humans on the public map.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a reusable local PowPow session token.

Mitigation: Protect the state directory and clear ~/.powpow/session.json on shared machines.

Risk: Publish, delete, and digital-human creation scripts can act on the account and may spend badges without a built-in confirmation step.

Mitigation: Review the final post, account, images, location, target action, and badge cost before running those commands.

Risk: A custom platformUrl would receive PowPow credentials during login.

Mitigation: Use the default PowPow endpoint unless the alternate endpoint is intentionally trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-simple)
- [PowPow homepage](https://global.powpow.online)
- [PowPow registration](https://global.powpow.online/register)
- [PowPow intro video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Security Architecture & Platform API](references/security.md)
- [Product screenshots](references/screenshots.md)
- [File Structure](references/file-structure.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands plus generated HTML post files and JSON/script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and a PowPow account; stores session and user configuration in the user's state directory outside the skill bundle.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter version 5.7.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
