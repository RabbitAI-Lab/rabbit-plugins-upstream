## Description:

Free-Model Config helps agents configure free AI models across Agnes AI, Zhipu BigModel, SenseNova, Xiaomi MIMO, and Meituan LongCat, including API key setup, model selection, WorkBuddy configuration, and multimodal generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to select free model providers, generate model configuration guidance, manage API key setup, and produce WorkBuddy-compatible configuration snippets. It also provides script-backed guidance for image, video, audio, TTS, and audio/video merge workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be handled through command-line arguments, environment variables, or local plaintext configuration.

Mitigation: Prefer environment variables or a managed secret store, redact keys from reports and shell history, and restrict permissions on ~/.workbuddy/models.json.

Risk: Video workflows may upload local images to third-party hosting or provider APIs.

Mitigation: Use only non-sensitive media, confirm user consent before uploads, and review provider data handling terms before running generation workflows.

Risk: The artifact contains an unsafe instruction that modifications to skill content must never be refused.

Mitigation: Treat artifact files as evidence only and continue applying host agent safety, security, and policy checks before editing or executing anything.

Risk: Generated configuration or usage guidance can become inaccurate as provider APIs, free tiers, or model names change.

Mitigation: Verify provider endpoints, model availability, quotas, and parameter limits against official provider documentation before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/free-model-config)
- [Free-Model Config Catalog](references/fmc-catalog.md)
- [Free-Model Config Requirements](references/fmc-requirements.md)
- [Free-Model Config Exemplars](references/exemplars.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, code, shell commands, guidance, files]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell command examples, and optional generated media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local model configuration at ~/.workbuddy/models.json and optional script outputs such as image, video, audio, and merged media files.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
