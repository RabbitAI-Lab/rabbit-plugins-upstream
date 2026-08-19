## Description:

Decode veterinary visit notes, discharge summaries, and lab panels into plain language, evaluate results against species-aware ranges, flag trends across visits, and prepare questions for the next veterinarian appointment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners and agents assisting them use this skill to organize veterinary notes, lab panels, kidney markers, breed-aware range checks, trends, and follow-up questions. It is for educational explanation and appointment preparation, not diagnosis, prescribing, emergency triage, or replacing the attending veterinarian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could mistake educational veterinary explanations for diagnosis or treatment advice.

Mitigation: Keep the disclaimer and veterinarian-confirmation framing in outputs, and route medical decisions, prescribing, and emergency triage to a veterinarian.

Risk: Pet records may include personal or clinic information that is unnecessary for explanation.

Mitigation: Ask users to provide only the information needed for species, breed, age, notes, lab values, units, and relevant visit history.

Risk: Reference ranges vary by lab, species, breed, age, and clinical context.

Mitigation: Compare outputs against the lab report's printed ranges and the attending veterinarian's interpretation, especially for abnormal findings and trends.

## Reference(s):

- [Veterinary Lab Reference Ranges](references/lab-ranges.md)
- [Veterinary Abbreviation Glossary](references/abbreviations.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text or Markdown summaries with abnormal-finding tables, trend notes, CKD staging details, and veterinarian question lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include an educational-use disclaimer and confirmation framing with a veterinarian.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact SKILL.md frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
