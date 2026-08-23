## Description:

Create and edit Walmart Marketplace product videos, assembly guides, package-content demonstrations, variant clips and retail advertising bases using Seedance generation and editing through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, retail content teams, and agent operators use this skill to generate and recut product listing videos, assembly guides, package-content proofs, variant clips, and retail ad bases while preserving catalog facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, videos, audio, and prompts are sent to AI Hive for remote processing.

Mitigation: Use this skill only when AI Hive data-handling obligations allow the asset transfer, and avoid confidential marketplace assets unless approved.

Risk: The skill can store an API key in ~/.ai-hive/config.json.

Mitigation: Prefer environment-variable or per-command API keys when persistent local credential storage is not desired.

Risk: Generated retail videos can misrepresent product facts, offer terms, availability, ratings, certifications, or package contents.

Mitigation: Review outputs against the item truth record and current Walmart Marketplace media and advertising requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/walmart-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key portal](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, video files]

**Output Format:** [Markdown guidance with bash commands; generated media is downloaded as video or image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials and may upload selected product images, videos, audio, and prompts for remote processing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
