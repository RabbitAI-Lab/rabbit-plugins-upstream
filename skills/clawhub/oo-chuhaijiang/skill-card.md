## Description:

Chuhaijiang connector for searching TikTok Shop products and retrieving product, creator, video, live stream, and review data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and inspect Chuhaijiang and TikTok Shop product intelligence through OOMOL's oo CLI with an already connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup points users to remote installer commands for the oo CLI without artifact-provided integrity checks.

Mitigation: Review the installer before use, prefer a verified or version-pinned installation source, and do not let an agent run remote installer commands automatically.

Risk: The connector operates through an OOMOL-connected Chuhaijiang account and can retrieve account-scoped market and product data.

Mitigation: Use an intended connected account, inspect each action schema before execution, and keep write or destructive action confirmation requirements if future actions are added.

## Reference(s):

- [Chuhaijiang homepage](https://www.chuhaijiang.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chuhaijiang)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Shell commands with JSON connector requests and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
