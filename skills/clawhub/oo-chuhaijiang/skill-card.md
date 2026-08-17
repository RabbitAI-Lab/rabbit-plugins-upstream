## Description:

出海匠 helps agents search and read Chuhaijiang TikTok Shop product, shop, creator, video, live, review, ranking, and similar-product data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for read-only Chuhaijiang product and market research, including TikTok Shop searches, rankings, new arrivals, promoted products, reviews, creators, videos, and live streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make external Chuhaijiang calls through the user's OOMOL-connected account.

Mitigation: Install it only when that account-backed data access is intended, and confirm ambiguous Chuhaijiang requests before making external calls.

Risk: First-time setup may require installing the oo CLI from an external installer.

Mitigation: Review the oo CLI installer before running setup, and run setup steps only after an auth, connection, or missing-command failure.

Risk: Connector payloads may drift if the live Chuhaijiang schema changes.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chuhaijiang)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [出海匠 homepage](https://www.chuhaijiang.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-focused connector actions inspect the live schema before sending JSON payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
