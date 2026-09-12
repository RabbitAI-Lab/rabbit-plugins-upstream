## Description:

Generates PRD files from a confirmed concept model only when the user explicitly invokes $concept-prd.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product teams use this skill to transcribe an explicitly confirmed concept model into PRD documentation: an overall PRD, per-concept CONCEPT.md files, and SYNCS.md grouped by flow. It is intended for documentation handoff after concept design, with model gaps returned upstream rather than filled in by the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PRD files may contain incorrect or incomplete specifications if the confirmed concept model is stale, ambiguous, or missing details.

Mitigation: Review the produced PRD, CONCEPT.md, and SYNCS.md files before committing, and send model gaps back to concept-design instead of accepting invented requirements.

Risk: The skill writes specification files into the repository.

Mitigation: Inspect the file changes before committing and confirm that each generated document maps to the intended concept model element.

## Reference(s):

- [Concept PRD ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/concept-prd)
- [Concept PRD Source Homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/concept-prd)
- [Templates Reference](references/templates.md)
- [Example Reserving Reference](references/example-reserving.md)
- [Sources Reference](references/sources.md)
- [WYSIWID Paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [conceptbox Course Template](https://github.com/61040-fa25/conceptbox)
- [Making Software Meaningful](https://arxiv.org/abs/2606.11051)
- [Verified LLM-Driven Synthesis for Concept Design](https://arxiv.org/abs/2607.15718)
- [Concept Rubric](https://61040-fa25.github.io/resources/concept-rubric)

## Skill Output:

**Output Type(s):** [Files, Markdown, Guidance]

**Output Format:** [Markdown PRD files and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes docs/prd/README.md, per-concept CONCEPT.md files, and SYNCS.md according to the confirmed model and bundled templates.]

## Skill Version(s):

0.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
