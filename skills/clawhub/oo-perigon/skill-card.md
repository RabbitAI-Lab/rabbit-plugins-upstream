## Description:

Enables agents to search and read Perigon news, entity, topic, source, journalist, company, people, and Wikipedia data, including semantic search and AI news summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Perigon through an OOMOL-connected account for news articles, story clusters, media sources, journalists, companies, people, topics, Wikipedia pages, semantic search results, and AI-generated news summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells users to execute a mutable remote installer directly in a shell.

Mitigation: Review the setup path before installing and prefer an already installed oo CLI or a pinned, signed, or checksum-verified installer.

Risk: Perigon queries and results flow through the OOMOL-connected account used by the skill.

Mitigation: Use an approved account connection and avoid sending sensitive queries unless the account and Perigon use are authorized.

## Reference(s):

- [ClawHub Perigon skill listing](https://clawhub.ai/oomol/skills/oo-perigon)
- [Perigon homepage](https://perigon.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action inputs and response shapes depend on the live Perigon connector schema and the user's connected OOMOL account.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
