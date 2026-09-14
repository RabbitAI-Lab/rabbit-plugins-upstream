## Description:

Generates realistic, dialogue-driven short-drama video clips from scripts or scene descriptions using the Ofox video API, with a creative brief, structured prompt, cost estimate, submission, polling, download, and cost reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a script beat or dialogue scene into a short realistic video clip with pre-generation choices, cost approval, and Ofox job handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Missing-dependency recovery guidance can lead to broad, unpinned global skill installation.

Mitigation: Install only ofox-video-core from a trusted, pinned source instead of using wildcard or broad global install commands.

Risk: Prompts, dialogue, and API-key-authorized generation are handled by Ofox's external service.

Mitigation: Review scene content before submission, avoid sensitive inputs, and rely on the approval gate before any paid generation is started.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-short-drama)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Project homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-short-drama)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured prompts, approval tables, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY and the curl and jq command-line tools.]

## Skill Version(s):

1.12.1 (source: server release evidence, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
