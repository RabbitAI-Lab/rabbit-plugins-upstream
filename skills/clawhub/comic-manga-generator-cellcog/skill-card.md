## Description:

Comic Generator helps agents use CellCog to create comics, manga, webtoons, graphic novels, comic strips, and other sequential art with character-consistent panels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to create comic and manga concepts, pages, strips, webtoon episodes, and graphic novel layouts through CellCog. It focuses prompts on panel planning, character consistency, style selection, and visual storytelling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CellCog API key could be exposed through prompts, logs, or committed files.

Mitigation: Store CELLCOG_API_KEY in the environment or an approved secret manager, and do not paste it into prompts or repositories.

Risk: The skill depends on CellCog service behavior and billing expectations.

Mitigation: Review CellCog's own skill or documentation before production use, especially SDK behavior, timeouts, and billing expectations.

## Reference(s):

- [Comic Generator on ClawHub](https://clawhub.ai/cellcog/skills/comic-manga-generator-cellcog)
- [CellCog Publisher Profile](https://clawhub.ai/user/cellcog)
- [CellCog](https://cellcog.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python examples, shell commands, and prompt guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call CellCog with creative chat mode and requires CELLCOG_API_KEY when used.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
