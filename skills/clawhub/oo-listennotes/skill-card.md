## Description:

Listen Notes (listennotes.com) lets an agent search and read podcast, episode, genre, language, region, ranking, and recommendation data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent retrieve Listen Notes podcast and episode information, including search results, typeahead suggestions, supported discovery filters, best-podcast rankings, and related podcast recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer patterns that can execute downloaded scripts.

Mitigation: Install the oo CLI manually from trusted official instructions, review the installer before running it, and avoid letting an agent execute curl|bash or irm|iex installer commands automatically.

Risk: The skill depends on an authenticated OOMOL-connected Listen Notes account.

Mitigation: Run Listen Notes actions only after the user has installed the CLI, signed in, and connected Listen Notes; use first-time setup steps only after an auth or connection failure.

## Reference(s):

- [Listen Notes homepage](https://www.listennotes.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-listennotes)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running Listen Notes actions and to return connector results as JSON.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
