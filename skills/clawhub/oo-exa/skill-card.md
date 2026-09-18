## Description:

Exa lets agents use an OOMOL-connected Exa account to search the web, fetch page contents, find similar pages, and generate citation-backed answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Exa search and content retrieval through an OOMOL-connected account when they need web search, page contents, similar URLs, or citation-backed answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL as the Exa connector broker and server-side credential handler.

Mitigation: Install only if that trust relationship is acceptable for the intended Exa account and data access.

Risk: First-time setup instructions include direct remote installer commands that execute installation code in a shell.

Mitigation: Review OOMOL's official installation instructions first and prefer a signed or package-manager install path when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-exa)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Exa homepage](https://exa.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return search results, page contents, similar-page matches, or citation-backed answers.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
