## Description:

Mediastack (mediastack.com). Use this skill for ANY Mediastack request - searching and reading data. Whenever a task involves Mediastack, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search live Mediastack news articles and news sources through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI that could execute changing external code.

Mitigation: Install the oo CLI manually from verified OOMOL documentation, inspect the installer source or signature/checksum when available, and do not allow an agent to run installer snippets automatically.

Risk: The skill depends on an OOMOL-connected Mediastack account and may require login, connection, or billing actions before use.

Mitigation: Approve account login, Mediastack connection, and billing recovery steps yourself before retrying connector actions.

## Reference(s):

- [Mediastack homepage](https://mediastack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mediastack)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing connector requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
