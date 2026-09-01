## Description:

Uses the Flyelep AI writing API to generate creative copy, optimize prompts, and provide writing inspiration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call Flyelep's assisted-generation API for product copy, prompt polishing, poster text, and short video script ideas. The skill can include up to six reference image URLs or upload local images before requesting writing options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded files are sent to the external Flyelep service.

Mitigation: Use non-confidential prompt text and images unless the user explicitly accepts sharing them with that service.

Risk: Uploaded local files are described as permanent public links.

Mitigation: Confirm before uploading local files, limit uploads to intended non-sensitive images, and reuse returned links instead of re-uploading the same file.

Risk: The skill requires a user-provided API key.

Mitigation: Request the key at runtime and avoid storing real keys in skill files, examples, logs, or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/ai-writing-assist)
- [Flyelep assisted generation API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/assistedGeneration)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns multiple creative copy options from the API and may include uploaded image URLs as request inputs.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
