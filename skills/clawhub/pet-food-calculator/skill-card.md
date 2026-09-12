## Description:

Calculate exact daily calorie needs and food portions for dogs and cats from species, breed, weight, age, activity level, and body condition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to estimate dog and cat daily feeding amounts, meal portions, treat budgets, food costs, transition schedules, and weight-loss timelines from user-supplied pet and food data. It is a local helper for feeding calculations and should not be used as veterinary diagnosis or prescription-diet advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Nutrition output may be mistaken for veterinary advice.

Mitigation: Present results as feeding-calculation support only, and direct users to a veterinarian for illness, prescription diets, unexplained weight changes, or refusal to eat.

Risk: Malformed or unrealistic numeric inputs can produce unsafe or invalid feeding results.

Mitigation: Ask for realistic positive inputs, especially species, weight, target weight, activity, and food kcal/kg, and have the user review results before acting on them.

Risk: Some advertised features are reference guidance or partial output rather than fully implemented automation.

Mitigation: Describe unsupported pieces as guidance and verify any schedule, cost, or weight-loss recommendation before relying on it.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/voronindenis5/pet-food-calculator)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/pet-food-calculator)
- [Energy Requirement Reference](references/energy-requirements.md)
- [Practical Feeding Guide](references/feeding-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON plan output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calculations depend on user-supplied species, weight, target weight, age, activity, and food kcal/kg.]

## Skill Version(s):

1.0.3 (source: server release metadata; skill frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
