## Description:

Tisane enables an agent to use the Tisane connector through the OOMOL oo CLI for text analysis, language detection, translation, paraphrasing, text extraction, semantic similarity, and entity comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when an agent needs to run Tisane text intelligence tasks through an OOMOL-connected account. It supports analysis of sentiment, entities, topics, problematic content, language segments, translation or paraphrasing, text extraction, semantic similarity, and entity comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute arbitrary code on the user's machine.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI only through a trusted, verifiable method controlled by the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tisane)
- [Tisane Homepage](https://tisane.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
