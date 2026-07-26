## Description: <br>
Turn recipes into a Todoist Shopping list by extracting ingredients from recipe photos or recipe web pages, comparing them against an existing Shopping project, skipping pantry staples by default, summing matching quantities when possible, and saving cooked recipes as Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[borahm](https://clawhub.ai/user/borahm) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to turn recipe photos or recipe web content into a flat Todoist Shopping list and a saved Markdown cookbook entry. It is useful when an agent needs to extract, normalize, deduplicate, and optionally add grocery items for a recipe workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recipe photos or recipe text are sent to Gemini for extraction and normalization. <br>
Mitigation: Avoid using sensitive recipe content and use --no-save when you do not want a local Markdown cookbook entry saved. <br>
Risk: The skill can create or update tasks in a Todoist Shopping project. <br>
Mitigation: Run with --dry-run first, review the proposed items, and only run without dry-run after confirming the Todoist target and extracted ingredients. <br>
Risk: The shell wrapper sources ~/.clawdbot/.env before running the Python script. <br>
Mitigation: Use the Python script directly or keep ~/.clawdbot/.env limited to the credentials this skill needs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/borahm/skills/recipe-to-list) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [JSON status output, Todoist task text, and Markdown cookbook files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or update Todoist Shopping tasks and write recipe Markdown entries; dry-run mode prints proposed items without creating tasks.] <br>

## Skill Version(s): <br>
0.1.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
