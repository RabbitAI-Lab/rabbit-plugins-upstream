## Description:

Generates traceable social-media video variants from an approved marketing master by adapting channel cuts, creating platform-native hooks, and extending tails for loops, CTAs, or disclaimer holds through AI Hive Seedance 2.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, creative, and developer operators use this skill to turn approved brand video assets into platform-specific variants for Douyin, Xiaohongshu, Reels, TikTok, Shorts, and similar channels while preserving brand invariants and review traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected marketing videos, images, and prompts to AI Hive for generation.

Mitigation: Use only media and prompts approved for AI Hive processing, and run with --preview first to inspect the model, sources, parameters, and full task before upload.

Risk: Generation jobs can be costly or submit unintended variants if arguments are wrong.

Mitigation: Use --preview before paid runs, keep campaign and variant identifiers traceable, and query the original taskId after timeouts instead of immediately resubmitting.

Risk: API keys may be exposed if stored on untrusted machines or in overly broad configuration files.

Mitigation: Store the API key only on trusted machines, pass it per command or through AI_HIVE_API_KEY when appropriate, and keep the local AI Hive config file restricted.

Risk: Generated marketing variants may alter product facts, claims, platform-safe zones, or legal/disclaimer presentation.

Mitigation: Review outputs against the approved master, brand source materials, required invariants, current platform rules, and approved post-production copy before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/social-media-marketing-video-generation-editing)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration, Files]

**Output Format:** [Markdown usage guidance with bash examples; preview and status commands emit JSON, and completed generation jobs can download MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports preview mode, API-key configuration, routing preferences, custom model parameters, optional download suppression, and custom output directories.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
