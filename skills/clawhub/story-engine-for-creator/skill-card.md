## Description:

A deterministic story architecture skill for causal plot reasoning, logic-gap detection, worldbuilding, narrative consistency checks, and presentation-layer audits.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, writers, narrative designers, and developers use this skill to turn story outlines into auditable causal chains, generate or repair chapters, check world and character consistency, and audit narration or dialogue issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Story text may be sent to a caller-attached LLM provider.

Mitigation: Attach only approved providers and avoid sending sensitive drafts unless that provider is permitted for the content.

Risk: The engine can write an HTML audit report to a caller-chosen local path.

Mitigation: Use workspace-scoped output paths and review generated files before sharing them.

Risk: The skill defaults to Chinese output unless configured otherwise.

Mitigation: Set the output language explicitly when the workflow requires another language.

Risk: The Creator engine warns that loading incompatible Creator and Business engine classes in one process can cause data errors or crashes.

Mitigation: Load only the intended engine namespace in a process unless the shared SecondPerspectiveCausalEngine is the only reused component.

## Reference(s):

- [Story Engine homepage](https://github.com/nohn3043-arch/story-engine)
- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/story-engine-for-creator)
- [Character to Narrative Link](references/CharacterToNarrativeLink.md)
- [Worldview Versioning](references/WorldviewVersioning.md)
- [Long Narrative Window Management](references/LongNarrativeWindow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Python API outputs, narrative text, audit dictionaries, repair guidance, and optional HTML audit reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to Chinese output unless configured otherwise; can use a caller-provided LLM provider for generation and repair.]

## Skill Version(s):

2.1.1 (source: server release evidence; artifact frontmatter reports 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
