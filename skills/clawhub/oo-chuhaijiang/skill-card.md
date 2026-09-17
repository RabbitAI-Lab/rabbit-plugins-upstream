## Description:

Use Chuhaijiang through an OOMOL-connected account to search and read TikTok Shop product, creator, video, live stream, and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Chuhaijiang from an agent through the oo CLI, including searching TikTok Shop products and reviewing product details, creators, videos, live streams, and customer reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI from a trusted, versioned release or package manager and verify signatures or checksums before use.

Risk: Chuhaijiang actions depend on an OOMOL-connected account and can expose account-scoped marketplace data to the agent session.

Mitigation: Use an account with appropriate access, inspect each live connector schema before execution, and avoid proactive authentication or connection changes unless a command fails for that reason.

## Reference(s):

- [Chuhaijiang homepage](https://www.chuhaijiang.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chuhaijiang)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Chuhaijiang icon](https://static.oomol.com/logo/third-party/chuhaijiang.svg)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before action execution; command results are returned as JSON with data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
