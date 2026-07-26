## Description: <br>
Import recipes into a self-hosted Mealie instance from a photo, text, or URL, with AI ingredient parsing and cover image upload. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maikimolto](https://clawhub.ai/user/maikimolto) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and self-hosting operators use this skill to turn recipe photos, text, or URLs into structured recipes in a Mealie instance, including ingredients, instructions, metadata, and cover images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Mealie API token that can create and update recipe-related data. <br>
Mitigation: Install only for trusted Mealie instances, scope and store the token carefully, and keep it in environment variables rather than skill files. <br>
Risk: Recipe text, images, or internal URLs may be parsed through Mealie's configured AI parser. <br>
Mitigation: Review Mealie's AI parser configuration before importing private recipes, images, or internal URLs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maikimolto/skills/mealie-recipe-import) <br>
- [Mealie](https://mealie.io) <br>
- [Skill workflow](SKILL.md) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a JSON job file and Python command sequence for creating or updating recipes through a user-provided Mealie API token.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
