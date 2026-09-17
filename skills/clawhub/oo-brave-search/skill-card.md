## Description:

Brave Search lets an agent query Brave Search web, image, news, and video indexes through the OOMOL-connected oo CLI without handling raw API tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route Brave Search requests through an OOMOL-connected account, inspect live action schemas, and run web, image, news, or video search actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer commands that could execute unverified code.

Mitigation: Install the oo CLI manually from trusted OOMOL documentation or a verified package, and do not let an agent run curl | bash or irm | iex installer commands automatically.

Risk: The skill depends on an authenticated OOMOL connection to Brave Search, so failed or expired credentials can interrupt use.

Mitigation: Run authentication or connection setup only after a command fails with an auth, scope, credential, app readiness, or billing error, then retry after the user intentionally completes the required setup.

## Reference(s):

- [Brave Search homepage](https://search.brave.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-brave-search)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and structured JSON response expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search action responses are described as JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
