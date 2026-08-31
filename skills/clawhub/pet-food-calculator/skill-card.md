## Description:

Calculate daily calorie needs and food portions for dogs and cats from species, breed, weight, age, activity level, and body condition, with cost comparisons, feeding schedules, and weight-loss flags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to estimate dog and cat feeding amounts, treat budgets, weight-loss timelines, food-transition schedules, and monthly food costs. It is intended for feeding estimates and should not replace veterinary care for illness, prescription diets, unexplained weight changes, or aggressive weight-loss plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Feeding estimates may be inappropriate for pets with illness, prescription diets, unexplained weight changes, or aggressive weight-loss needs.

Mitigation: Use the output as an estimate and consult a veterinarian for those cases, especially for cats and weight-loss plans.

Risk: The local calculator can write a JSON feeding plan to a path selected by the user.

Mitigation: Choose an intended output path and review generated files before relying on or sharing them.

## Reference(s):

- [Energy Requirement Reference](references/energy-requirements.md)
- [Practical Feeding Guide](references/feeding-guide.md)
- [Server-Resolved Source Repository](https://github.com/voronindenis5/pet-food-calculator)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/pet-food-calculator)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or plain text feeding plans, optional JSON plan files, and runnable Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a JSON feeding plan to a user-selected local path when the JSON output option is used.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
