## Description:

Calculates daily calorie needs and food portions for dogs and cats from species, weight, age, activity level, and body condition, with cost comparisons, feeding schedules, food-transition guidance, and weight-loss flags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to calculate dog and cat feeding amounts, estimate treat budgets and food costs, generate transition schedules, and plan safer weight-loss targets from pet and food-label inputs. It is planning support and not a substitute for veterinary care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local calculator script may write a JSON report to a user-specified path.

Mitigation: Keep output paths inside a safe workspace and review generated files before reusing them.

Risk: Feeding or weight-loss calculations can be misused as veterinary advice.

Mitigation: Treat results as planning help, and consult a veterinarian for illness, prescription diets, unexplained weight changes, or a cat refusing food.

Risk: Incorrect pet weight, target weight, or food kcal/kg inputs can produce misleading portions.

Mitigation: Verify food-label calories and target weight before using the plan, then recheck portions as weight changes.

## Reference(s):

- [Energy Requirement Reference](references/energy-requirements.md)
- [Practical Feeding Guide](references/feeding-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/pet-food-calculator)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text feeding plan, optional JSON report, and Markdown guidance with CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a JSON report to a user-specified path when requested.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
