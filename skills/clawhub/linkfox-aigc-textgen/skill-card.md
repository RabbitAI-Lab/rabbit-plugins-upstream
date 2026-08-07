## Description:

Generates text from prompts with optional image or video URL context using LinkFox large-language-model services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate copy, translations, summaries, data-analysis text, and image or video content analysis through LinkFox text-generation APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, media URLs, task metadata, and feedback content are sent to LinkFox services.

Mitigation: Do not include secrets, credentials, or personal data unless the user explicitly intends to send that information to LinkFox.

Risk: The skill may direct an agent to install a remote onboarding skill or chain generated text into image or video generation.

Mitigation: Require user review before installing onboarding assets or invoking downstream media-generation skills, and inspect generated parameters before execution.

## Reference(s):

- [AI Text Generation API Reference](artifact/references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-textgen)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON responses, or a JSON envelope pointing to a saved response file for large outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content newlines may be replaced with the single-character placeholder ⏎ for shell-safe chaining; large responses can be saved under a local LinkFox session path.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
