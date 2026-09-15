## Description:

Transcribes a confirmed concept model into traceable PRD and colocated specification files when the user explicitly invokes $concept-prd.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to persist an already-confirmed concept model as an overall PRD, concept specifications, synchronization rules, and acceptance provenance without redesigning the model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documentation edits could misstate the confirmed model, legacy content, or acceptance provenance.

Mitigation: Review generated PRD, CONCEPT, and SYNCS edits against the confirmed model and requirement sources before accepting them.

Risk: Open decisions or missing application goals could be mistaken for resolved requirements.

Mitigation: Keep marked gaps open until they are confirmed by the appropriate product or design authority.

## Reference(s):

- [Concept PRD homepage](https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-prd)
- [Transcription Sources](references/sources.md)
- [Concept and Synchronization Specification Contract](references/spec-format.md)
- [File Layout for CONCEPT and SYNCS](references/templates.md)
- [Reservation Transcription Example](references/example-reserving.md)
- [Concept Purposes and Synchronization](https://essenceofsoftware.com/posts/distillation/)
- [Jackson 2015 concept essay](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf)
- [WYSIWID](https://arxiv.org/abs/2508.14511)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown PRD, CONCEPT, and SYNCS documentation with traceability notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User-invoked only; preserves open decisions and acceptance provenance rather than resolving missing model facts.]

## Skill Version(s):

0.5.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
