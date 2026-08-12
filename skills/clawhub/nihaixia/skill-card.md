## Description:

A Chinese-language agent skill that helps answer from a curated knowledge base about Ni Haixia's classical Chinese medicine teachings, including Shanghan Lun, Jingui Yaolue, Huangdi Neijing, acupuncture, materia medica, and case notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jangviktor-web](https://clawhub.ai/user/jangviktor-web)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and summarize a Chinese-language reference collection on Ni Haixia's academic style and classical Chinese medicine materials. It should be treated as historical or educational reference material, not as a source for medical diagnosis, prescribing, emergency care, or advice to avoid conventional care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can elicit concrete diagnosis, herbal dosing, acupuncture, emergency, cancer, or heart-disease treatment guidance.

Mitigation: Use only with medical safety safeguards that keep outputs educational, avoid diagnosis or prescribing, and direct urgent or serious symptoms to qualified care.

Risk: Case notes and historical medical claims may be mistaken for patient-specific medical advice.

Mitigation: Frame case material as historical reference and avoid applying it to identifiable people or current clinical decisions.

Risk: The artifact includes strong viewpoints about medical systems that could encourage avoidance of conventional care.

Mitigation: Require neutral wording and prevent advice that discourages emergency services, licensed clinicians, or evidence-based care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jangviktor-web/skills/nihaixia)
- [Distilled reference README](references/distilled/README.md)
- [Six-meridian formulas quick reference](references/distilled/01-six-meridian-formulas.md)
- [Acupuncture quick reference](references/distilled/02-acupuncture-quick-ref.md)
- [Clinical experience notes](references/distilled/03-clinical-experience.md)
- [Distillation audit notes](references/distilled/audit-notes.md)
- [Research combined reference](references/research/combined_reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are grounded in the bundled Chinese-language knowledge base and may include formula, herb, acupuncture, or case references; medical safety constraints should be applied before user-facing use.]

## Skill Version(s):

2.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
