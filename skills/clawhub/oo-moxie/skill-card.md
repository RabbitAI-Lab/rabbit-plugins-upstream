## Description:

Moxie (withmoxie.com). Use this skill for ANY Moxie request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Moxie workspace data through an OOMOL-connected account, including clients, contacts, projects, pipeline stages, and task stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to run remote installer scripts, which creates supply-chain risk if the endpoint or script is not trusted.

Mitigation: Review the installer path before installation and prefer a trusted, pinned package or verified release of the oo CLI.

Risk: The skill reads connected Moxie workspace data through an authenticated OOMOL account.

Mitigation: Inspect the live action schema before each request and use the disclosed read and search actions unless the user explicitly approves a state-changing action.

## Reference(s):

- [Moxie ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moxie)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Moxie homepage](https://www.withmoxie.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
