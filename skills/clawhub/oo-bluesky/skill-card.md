## Description:

Bluesky operates a connected Bluesky account through OOMOL's oo CLI for creating text posts, viewing profiles and timelines, and searching posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to complete Bluesky account tasks from an agent, including reading timelines, looking up profiles, searching posts, and preparing text posts for confirmed publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute remote installer scripts.

Mitigation: Use a reviewed, version-pinned, checksum-verified installer path before running oo CLI setup.

Risk: The create_text_post action changes state in the authenticated Bluesky account.

Mitigation: Confirm the exact post content and intended effect with the user before running the write action.

## Reference(s):

- [ClawHub Bluesky skill page](https://clawhub.ai/oomol/skills/oo-bluesky)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bluesky homepage](https://bsky.social)
- [OOMOL Bluesky connection setup](https://console.oomol.com/app-connections?provider=bluesky)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Bluesky connector JSON responses containing data and an executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
