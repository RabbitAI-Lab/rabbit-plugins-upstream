## Description:

Publishes user-provided photos or travel material as PowPow travelogue posts, and creates chat-capable digital humans pinned to the public map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn travel photos, finished text, or raw trip material into PowPow posts, with optional place tags, images, and digital-human tags. Users can also create a map-pinned digital human from a name, persona, and location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles PowPow credentials and keeps a local session token.

Mitigation: Use the skill only in a trusted agent environment, protect POWPOW_STATE_DIR like a credential store, and clear or rotate the session when access is no longer needed.

Risk: The skill can publish or delete public PowPow posts and create badge-consuming digital humans using the logged-in account.

Mitigation: Review drafts, image lists, locations, and digital-human creation details before approving execution, especially on hosts without separate approval controls.

## Reference(s):

- [PowPow homepage](https://global.powpow.online)
- [PowPow map](https://global.powpow.online/map)
- [Chinese edition on ClawHub](https://clawhub.ai/durenzidu/skills/powpow-simple)
- [Security architecture](references/security.md)
- [Product screenshots](references/screenshots.md)
- [Changelog](references/changelog.md)
- [File structure](references/file-structure.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with shell commands, generated post HTML drafts, local preview files, and published PowPow links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and a PowPow account; writes session state to POWPOW_STATE_DIR rather than the skill bundle.]

## Skill Version(s):

1.0.0 (source: frontmatter, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
