## Description:

Multimodal Gen helps agents structure prompts and invocation guidance for text-to-image, image-to-image, text-to-video, image-to-video, and speech-to-text tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external users use this skill to turn multimodal content requests into structured prompts and invocation guidance for image, video, and authorized audio transcription workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learning helper can persist free-form user preferences, errors, usage notes, or operational context in learned_patterns.json.

Mitigation: Avoid recording sensitive prompts, personal data, credentials, or confidential operational details, and periodically review or delete learned_patterns.json.

Risk: Generated image, video, or transcription workflows can involve copyright, consent, or platform-policy constraints.

Mitigation: Use only authorized source media, confirm commercial rights for generated assets, and apply the skill's stated content-safety boundaries before publication or reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/multimodal-gen)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with prompt text, inline shell commands, and helper-script JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The prompt helper emits optimized prompt text and a JSON payload; the learning helper can write learned_patterns.json in the selected skill directory.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
