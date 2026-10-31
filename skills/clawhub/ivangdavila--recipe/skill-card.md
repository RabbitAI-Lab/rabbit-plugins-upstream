## Description:

Recipes captures, standardizes, scales, and files recipes into a local personal collection that stays searchable and cookable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to capture recipes from links, photos, videos, dictation, handwritten cards, and app exports, then normalize them into a searchable local collection. It also supports scaling, unit conversion, substitution, equipment rewrites, weekly planning, shopping-list aggregation, costing, testing notes, family-recipe preservation, and recipe migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may retain allergies, diet-relevant conditions, guest restrictions, kitchen facts, prices, and project notes in shared local files.

Mitigation: Review the configured local data files periodically and avoid providing health or guest details unless they should be retained.

Risk: Captured recipe material may include credentials or paid-site content from user-provided exports or sync settings.

Mitigation: Store recipe content with attribution, do not bypass paywalls, and strip API keys, sync tokens, logins, card numbers, addresses, and other secrets before writing local notes.

Risk: Food substitutions or recipe adaptations can create safety issues when allergies, intolerances, or conditions are incomplete or stale.

Mitigation: Read the shared health profile before proposing food the user will eat, name allergens explicitly, mark substitutions as untested until cooked, and refer changing medical restrictions to a clinician.

## Reference(s):

- [ClawHub Recipes Skill](https://clawhub.ai/ivangdavila/skills/recipe)
- [Clawic Recipes Page](https://clawic.com/skills/recipe)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown recipe files, index rows, plans, shopping lists, costing notes, configuration updates, and plain-text guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains local plain-text recipe data and shared local health, contact, and project notes when relevant.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
