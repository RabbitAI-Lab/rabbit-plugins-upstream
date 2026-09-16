## Description:

Use this skill to operate RiteKit through the OOMOL oo CLI for hashtag suggestions, trending hashtag discovery, engagement statistics, and banned Instagram hashtag cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate RiteKit through an OOMOL-connected account for hashtag suggestions, trending hashtag discovery, engagement statistics, and banned Instagram hashtag cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unpinned remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Install the oo CLI only from a trusted source, and prefer a pinned, signed, or package-manager installation path before running RiteKit actions.

Risk: RiteKit requests depend on an OOMOL-connected account and server-side credential handling.

Mitigation: Use the documented connector schema command before each action and avoid exposing raw credentials in prompts, payloads, logs, or local files.

## Reference(s):

- [RiteKit homepage](https://ritekit.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ritekit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live RiteKit connector schemas and server-side credential handling through OOMOL.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
