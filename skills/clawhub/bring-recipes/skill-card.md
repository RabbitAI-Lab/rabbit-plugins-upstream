## Description: <br>
Browses Bring! recipe inspirations and recipe metadata from the CLI, with filtering and JSON output but no ingredient import because the API does not provide ingredient lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darkdevelopers](https://clawhub.ai/user/darkdevelopers) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to discover Bring! recipe inspirations, inspect recipe metadata such as names, authors, types, images, links, and tags, and request JSON output for scripting. It is browse-only and should not be used for ingredient import or shopping-list management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bring credentials may be exposed if the password environment variable is stored in shared profiles, logs, or CI. <br>
Mitigation: Use credentials only in a trusted local shell, avoid shared profiles and CI, and unset or rotate the password if exposure is possible. <br>
Risk: The CLI source or npm dependencies may contain behavior not visible in the skill instructions. <br>
Mitigation: Inspect the actual CLI source and npm dependencies before installing or running the skill. <br>
Risk: Users may expect ingredient lists or shopping-list changes that the Bring Inspirations API does not provide. <br>
Mitigation: Use the skill only for browsing recipe metadata and manually add ingredients or shopping-list items through another workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/darkdevelopers/skills/bring-recipes) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Bring account credentials through BRING_EMAIL and BRING_PASSWORD; outputs browse-only recipe metadata, not ingredient lists.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
