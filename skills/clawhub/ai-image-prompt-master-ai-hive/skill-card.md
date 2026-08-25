## Description:

Turns vague ecommerce, advertising, and social image needs into structured bilingual AI image prompts, negative constraints, reference-image strategies, model guidance, and optional AI-HIVE generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, designers, and content creators use this skill to turn product, campaign, and social-media image requirements into reviewable visual briefs, prompts, model choices, and execution commands. It is suited for ecommerce, advertising, marketing, short-video, comic, livestream commerce, and social recommendation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an AI-HIVE API key on the local machine.

Mitigation: Use an environment variable when possible, keep ~/.ai-hive/config.json private, and remove that file when the key should no longer be stored on the machine.

Risk: AI-HIVE generation commands may make networked, potentially billable API calls.

Mitigation: Review prompts, model parameters, routing mode, and price snapshots before execution; start with a small sample before batch generation.

Risk: Reference media or commercial claims may be unauthorized, misleading, or unsuitable for the target platform.

Mitigation: Use only authorized source media and verify product facts, claims, logos, and platform requirements before publishing generated assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-image-prompt-master-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown response with inline shell commands and optional JSON or downloaded media file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce blueprint JSON, prompt variants, task records, AI-HIVE configuration steps, and generated-media download locations when the user chooses to run commands.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
