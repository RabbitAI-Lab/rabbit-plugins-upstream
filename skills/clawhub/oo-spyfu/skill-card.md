## Description:

SpyFu enables an agent to search and read SpyFu domain, competitor, keyword, SERP, advertising history, ranking, and usage data through an authenticated OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SpyFu through an authenticated OOMOL connection for SEO and PPC research, including domain discovery, competitor analysis, keyword metrics, SERP analysis, ranking history, top pages, ad history, and usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include mutable remote installer scripts that could change after review.

Mitigation: Review the installer before use, or install the oo CLI through a verified package or downloaded installer with checksum or signature validation.

Risk: SpyFu access depends on an intentionally connected OOMOL account and may fail when authentication, scopes, credentials, or billing are unavailable.

Mitigation: Run connector actions only after the user has installed the CLI, signed in, connected SpyFu, and resolved any billing or connection errors.

## Reference(s):

- [ClawHub SpyFu skill](https://clawhub.ai/oomol/skills/oo-spyfu)
- [SpyFu homepage](https://www.spyfu.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [SpyFu icon](https://static.oomol.com/logo/third-party/spyfu.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent outputs are based on live connector schemas and SpyFu query responses.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
