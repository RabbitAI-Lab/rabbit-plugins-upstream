## Description:

Generates or edits images with specified Chinese, English, numeric, or multilingual text using GPT Image 2 through AI Hive, with guidance to manually verify every character, digit, and punctuation mark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and agent operators use this skill to create posters, packaging, menus, infographics, ads, and localized visuals where visible text needs tight control. It is best suited for drafting and editing image assets that will still receive human text QA before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the third-party AI Hive provider.

Mitigation: Use the skill only with content approved for AI Hive processing, and avoid sending confidential or regulated material unless the user's policies permit it.

Risk: The skill stores an AI Hive API key locally for CLI use.

Mitigation: Prefer environment variables or ensure the local config file remains restricted to the current user, and rotate the key if it may have been exposed.

Risk: Image models can render incorrect, missing, duplicated, or misleading text despite exact-text prompts.

Mitigation: Manually compare generated images against the approved copy, and use professional layout tools for high-risk legal, medical, financial, pricing, certification, or compliance text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-exact-text-image)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and generated image files downloaded by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts, optional reference images, batch size, routing mode, model parameters, output directory, and task IDs; generated images are downloaded as files unless no-download mode is selected.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
