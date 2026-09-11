## Description:

p-video-edit helps agents edit an existing video from a text instruction, including recoloring, restyling, object or text changes, lighting changes, and optional reference-guided edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to prepare request-locked prompts and Pruna API calls for editing an existing source video up to 15 seconds while preserving unrequested elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media and edit prompts are sent to Pruna's API using a Pruna API key.

Mitigation: Confirm the user is comfortable sending the selected media to Pruna, avoid sensitive media unless authorized, and keep PRUNA_API_KEY out of prompts, logs, and shared artifacts.

Risk: The skill documents unpinned companion skill installs that can add mutable external instructions to the agent environment.

Mitigation: Review or pin companion skill installs before use, and install only trusted versions that match the intended workflow.

Risk: Weak or broad edit requests can produce poor results or unintended changes to the source video.

Mitigation: Keep one principal change per run, preserve explicit keep clauses, and show the prompt before paid API calls when wording is not locked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-video-edit)
- [Pruna files API endpoint](https://api.pruna.ai/v1/files)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and curl command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompt, upload, prediction request, polling, and download guidance; does not generate video directly.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
