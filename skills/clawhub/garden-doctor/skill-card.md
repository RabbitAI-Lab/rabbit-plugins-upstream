## Description:

Diagnoses plant problems from symptoms (yellow leaves, brown spots, drooping, pests). Provides likely diagnoses with confidence scores, treatment plans, and prevention tips using a knowledge base of 40+ common plant problems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Gardeners, plant caretakers, and agents assisting with horticulture triage use this skill to match reported plant symptoms to likely causes, treatment steps, and prevention tips. It is informational guidance and is not a substitute for professional review for valuable, rare, edible, or commercially important plants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant diagnosis and treatment guidance may be incorrect or incomplete for valuable, rare, edible, or commercially important plants.

Mitigation: Use the output as informational guidance, verify the diagnosis, and consult a horticulturist or agricultural extension service when stakes are high.

Risk: Suggested treatments can include fungicides, insecticides, oils, rubbing alcohol, or plant removal.

Mitigation: Follow product labels and local rules, keep treatments away from children and pets, and avoid chemical treatment when uncertain.

## Reference(s):

- [Plant Problem Knowledge Base](references/knowledge-base.md)
- [Symptoms Guide](references/symptoms-guide.md)
- [Server-resolved source repository](https://github.com/voronindenis5/garden-doctor)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/garden-doctor)

## Skill Output:

**Output Type(s):** [JSON, guidance, text]

**Output Format:** [Structured JSON and command-line text containing likely diagnoses, confidence scores, treatment steps, prevention tips, and an informational disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnosis quality depends on the symptoms supplied by the user and the built-in plant problem knowledge base.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
