## Description:

Suggests recipes based on leftover ingredients the user already has, ranking matches by how completely the available ingredients satisfy each recipe and flagging missing ingredients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and agent developers use this skill to turn text, photo-description, or voice-derived ingredient lists into practical recipe suggestions, including missing ingredient notes and substitution ideas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Substitution suggestions may be unsafe for people with allergies, intolerances, religious or dietary restrictions, or food-safety constraints.

Mitigation: Treat substitutions as suggestions only and ask the user to verify dietary restrictions, allergen exposure, and food safety before cooking.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/leftover-chef)
- [Source repository](https://github.com/voronindenis5/leftover-chef)
- [Recipe Notes](references/recipes.md)
- [Ingredient Substitutions](references/substitutions.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with optional command-line output or JSON recipe matches]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranks recipe matches by usage percentage and includes available ingredients, missing ingredients, preparation metadata, and substitution guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
