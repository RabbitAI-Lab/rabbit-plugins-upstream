## Description:

Dlazy Audio音频生成 helps agents use the dlazy CLI to route prompts and selected media inputs to hosted audio models for text-to-speech, music, sound effects, and voice cloning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and automation teams use this skill to generate audio assets through hosted dLazy models, including narration, short-form music, sound effects, and cloned-voice TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy-hosted services for generation.

Mitigation: Use only content you intend to upload to dLazy services, and avoid private media, secrets, sensitive internal content, and unauthorized voice samples.

Risk: API keys and callback URLs can expose account access or send generated outputs to unintended destinations.

Mitigation: Configure credentials through approved local or environment-based mechanisms, never paste secrets into chat, and provide only callback URLs you control and trust.

Risk: Generated or cloned audio can raise authorization, copyright, or impersonation concerns.

Mitigation: Use source media and voice samples only with appropriate rights and consent, and review generated content before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dlazy-audio-generate)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON result handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce hosted file URLs or local audio filenames through dlazy command output; requires dLazy API key configuration.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
