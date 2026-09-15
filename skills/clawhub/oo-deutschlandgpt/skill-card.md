## Description:

Operate DeutschlandGPT through the OOMOL connector for reading, creating, and updating data without handling raw API tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate DeutschlandGPT through an OOMOL-connected account for chat completions, embeddings, and enabled model discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded code immediately.

Mitigation: Install the oo CLI only from a trusted, independently verified source before using the skill, and avoid running the remote installer commands unless the installer has been reviewed and approved.

Risk: Write-tagged DeutschlandGPT actions can create chat completions or embeddings in the connected workspace.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

## Reference(s):

- [DeutschlandGPT homepage](https://www.deutschlandgpt.de/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-deutschlandgpt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects returned by the oo CLI when actions are run.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
