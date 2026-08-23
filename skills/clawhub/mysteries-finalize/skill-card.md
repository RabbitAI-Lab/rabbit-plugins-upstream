## Description:

This skill helps finalize Farsight video projects by verifying required media assets, generating transcripts and localized subtitles, creating thumbnail variants, and organizing final files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External media operators use this skill to prepare Farsight release assets by verifying required final video, audio, and thumbnail files, then producing transcripts, subtitles, thumbnail variants, and organized final folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow modifies and organizes media outputs under the selected project's Renders/Final directory.

Mitigation: Confirm the correct project directory and the required video, audio, and thumbnail files before execution.

Risk: Subtitle localization may send subtitle content through the translation provider used by deep-translator.

Mitigation: Confirm the subtitle content is acceptable for that provider before running localization.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed by an agent, the workflow produces transcript text, subtitle files, and thumbnail image variants under Renders/Final.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
