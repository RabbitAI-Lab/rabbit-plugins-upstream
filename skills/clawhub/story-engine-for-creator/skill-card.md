## Description:

Deterministic plot architecture tool with built-in Second Perspective causal reasoning, logic vulnerability detection, automatic worldbuilding generation, narrative presentation layer audit, foreshadowing ledger, spacetime consistency check, hash-chained audit reports, and incremental diff-only audit.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and writing teams use this skill to design, generate, and audit fiction plots for novels, game scripts, screenplays, and long-form IP continuity. It helps check causal logic, character behavior, worldbuilding consistency, foreshadowing closure, spacetime conflicts, and narrative presentation issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private drafts, outlines, character data, and audit prompts may be sent to a remote LLM endpoint when OpenAIProvider is explicitly attached.

Mitigation: Keep the skill offline by default for private drafts, and attach a remote provider only when that data transfer is intended and approved.

Risk: Generated fiction and audit results may contain incorrect, incomplete, unsafe, or publication-inappropriate content.

Mitigation: Use the output as drafting and consistency assistance, and apply human editorial, legal, policy, and safety review before publishing or sharing.

Risk: Artifact licensing text restricts use to personal non-commercial research unless written commercial authorization is obtained.

Mitigation: Confirm the authoritative license and obtain required authorization before commercial deployment or redistribution.

Risk: Some long-narrative checkpoint concepts are documented as design-level material rather than fully implemented behavior.

Mitigation: Rely on implemented audit outputs such as foreshadow SET/PAY reconciliation, spacetime checks, and hash-chained audit reports, and review design-level claims manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/story-engine-for-creator)
- [Project homepage](https://github.com/nohn3043-arch/story-engine)
- [Character to Narrative Link](artifact/references/CharacterToNarrativeLink.md)
- [Long-Narrative Window Management](artifact/references/LongNarrativeWindow.md)
- [Worldview Versioning](artifact/references/WorldviewVersioning.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with Python snippets, generated narrative text, structured audit dictionaries, and optional HTML audit reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default; remote LLM calls occur only when an OpenAI-compatible provider is explicitly configured.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
