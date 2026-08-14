## Description:

Suggests recipes based on leftover ingredients the user already has, ranking matches by ingredient coverage and flagging missing ingredients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to turn a list, photo description, or voice inventory of available ingredients into ranked recipe suggestions. It helps identify meals that can be cooked immediately or with a small number of substitutions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recipe and substitution suggestions may not account for allergies, dietary restrictions, or medical nutrition needs.

Mitigation: Ask users to confirm allergies and dietary requirements before recommending recipes or substitutions, and avoid presenting the output as medical or nutrition advice.

Risk: General cooking guidance may not cover all food-safety requirements for a user's ingredients, storage history, or local standards.

Mitigation: Advise users to verify freshness, storage, cooking temperatures, and ingredient suitability before preparing or eating suggested recipes.

## Reference(s):

- [Recipe Notes](references/recipes.md)
- [Ingredient Substitutions](references/substitutions.md)
- [Source repository](https://github.com/voronindenis5/leftover-chef)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/leftover-chef)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown recipe recommendations with optional JSON matcher output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked recipe matches include ingredient coverage, missing ingredients, recipe metadata, and substitution guidance.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
