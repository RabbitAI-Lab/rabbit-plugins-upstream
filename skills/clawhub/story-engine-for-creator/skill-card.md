## Description:

A deterministic story-architecture skill for causal reasoning, plot-hole detection, worldbuilding generation, and narrative presentation auditing.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, writers, game narrative designers, and script developers use this skill to structure long-form stories, check causal consistency, audit character behavior, manage world rules, and generate or repair narrative content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manuscript text, character data, world rules, or repair issues may be sent to an external provider if a real LLMProvider is configured.

Mitigation: Use the local default behavior for confidential drafts, or connect only trusted providers with acceptable data-handling terms.

Risk: Narrative audit and repair suggestions may be incorrect or may not match the creator's intent.

Mitigation: Review proposed plot repairs, world-rule changes, and dialogue edits before applying them to a manuscript or script.

Risk: Loading Creator and Business engines in the same process can mix incompatible data classes and corrupt results.

Mitigation: Keep Creator and Business engine modules isolated unless sharing only the documented SecondPerspectiveCausalEngine component.

## Reference(s):

- [Character to Narrative Link](references/CharacterToNarrativeLink.md)
- [Worldview Versioning](references/WorldviewVersioning.md)
- [Long-Narrative Window Management](references/LongNarrativeWindow.md)
- [Project homepage](https://github.com/nohn3043-arch/story-engine)
- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/story-engine-for-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and text guidance with Python code examples and structured audit outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default; external LLM-provider behavior depends on user configuration.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact SKILL.md frontmatter reports 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
