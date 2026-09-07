## Description:

Transcribes a confirmed concept model into PRD specs: a central overall PRD, wyx-compatible colocated CONCEPT.md files, and flow-grouped SYNCS.md content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to turn confirmed concept-design models into navigable PRD documentation without adding model content. It is suited for producing an overall PRD, per-concept specs, and flow-grouped sync documentation before implementation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PRD files can introduce incorrect or misleading guidance if the source concept model is incomplete or the request is only loosely related to concept PRD work.

Mitigation: Review generated documents against the confirmed concept-design model before committing, and send gaps back to concept-design instead of filling them in.

Risk: The trigger wording can activate the skill for generic specification requests.

Mitigation: Confirm the user wants a concept PRD workflow before applying the templates and output structure.

## Reference(s):

- [Skill source](SKILL.md)
- [CONCEPT.md and SYNCS.md templates](references/templates.md)
- [Concept specification sources](references/sources.md)
- [WYSIWID paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects](https://arxiv.org/abs/2606.27258)
- [conceptbox course template](https://github.com/61040-fa25/conceptbox)

## Skill Output:

**Output Type(s):** [markdown, guidance]

**Output Format:** [Markdown files and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an overall PRD, per-concept CONCEPT.md files, and flow-grouped SYNCS.md content from confirmed concept-design inputs.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
