## Description:

Localizes shared product assets for multiple regions with multilingual copy, size conversion tables, regional compliance label guidance, and adapted marketplace images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers and localization teams use this skill to adapt product copy, size charts, and product imagery for selected markets and marketplaces. Its regional compliance notes are prompts for further review, and the skill recommends human review of translated image text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports medium confidence and partial coverage: 6 of 10 components were fully inspected and 4 were partial.

Mitigation: Review commands and files that were only partially inspected before use.

Risk: Prompts and supplied images may be sent to an external image-generation service selected for the task.

Mitigation: Choose a provider whose data handling fits the material, and avoid sending sensitive images or information unless permitted.

Risk: The security guidance calls out an unpinned command and a broad skill trigger.

Mitigation: Review commands before execution and invoke the skill only when localization is intended.

## Reference(s):

- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Text, Tables, Files, Shell commands, Guidance]

**Output Format:** [PNG or JPEG product images, localized text and size tables, Markdown guidance, CLI commands, and image validation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image files are saved to the requested path; review generated non-English image text and confirm current marketplace requirements before listing.]

## Skill Version(s):

1.0.31 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
