## Description:

Diagnoses cohesion in the Discussion section of an English psychology research paper across local cohesion devices and global narrative thread, without generating or rewriting prose.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laninga](https://clawhub.ai/user/laninga)

### License/Terms of Use:

MIT-0

## Use Case:

External authors, editors, and academic-writing reviewers use this skill to diagnose local cohesion devices and global narrative flow in Discussion sections of English psychology research papers. The skill is intended for objective diagnostic feedback, not prose generation or rewriting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may invoke the skill when the user wanted a rewrite or a different type of writing review.

Mitigation: Confirm that the requested task is a Discussion-section cohesion diagnosis before applying the rubric.

Risk: Diagnostic feedback could be misapplied to documents outside the skill's stated scope of English psychology Discussion sections.

Mitigation: Use the findings as scoped writing diagnostics and avoid treating them as authoritative review for other disciplines or article sections.

Risk: Users may expect the skill to produce replacement prose.

Mitigation: Keep outputs diagnostic and issue-focused; do not generate or rewrite the user's Discussion text.

## Reference(s):

- [Cohesion Rubric](artifact/references/rubric.md)
- [Cohesion Checklist](artifact/references/checklist.md)
- [Example: Mechanical Connective Chain](artifact/references/examples/bad_ayanian_2020_mechanical_chain.md)
- [Example: Synthetic Abrupt Transitions](artifact/references/examples/bad_synthetic_abrupt_transitions.md)
- [Example: Multi-Study Synthesis Connectives](artifact/references/examples/good_ayanian_2020_first_second.md)
- [Example: Predictive Roadmap](artifact/references/examples/good_costello_2021_unpack_sequence.md)
- [Example: Adversative Transition](artifact/references/examples/good_ebert_2020_however_transition.md)
- [Example: Sequential Connectives](artifact/references/examples/good_midgley_2020_sequential_connectives.md)
- [ClawHub skill page](https://clawhub.ai/laninga/skills/discussion-cohesion-diagnosis)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown diagnostic report with scored cohesion sections and prioritized issue list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostic feedback only; the skill does not generate or rewrite the submitted Discussion text.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
