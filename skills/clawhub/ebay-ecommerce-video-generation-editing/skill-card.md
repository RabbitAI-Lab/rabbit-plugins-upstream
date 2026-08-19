## Description:

Create and edit eBay listing videos that document exact-item condition, defects, functional tests, included accessories, refurbished work, and collectible details using conservative AI Hive video generation and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External eBay sellers and listing operators use this skill to create or edit product videos that preserve exact-item evidence, condition details, defects, functional tests, included accessories, and refurbishment records. The skill is intended for conservative listing-media workflows where real item evidence should not be beautified or replaced by generated claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected listing photos, videos, and prompts are sent to AI Hive for remote processing.

Mitigation: Use only media and prompts that the seller is comfortable sharing with AI Hive, and avoid confidential seller or buyer data.

Risk: An AI Hive API key may be stored locally.

Mitigation: Prefer environment-variable or permission-restricted configuration, rotate exposed keys, and remove keys from shared machines.

Risk: Generated or edited listing videos can misrepresent item condition, defects, authenticity, warranty, or included accessories if prompts are not constrained.

Mitigation: Retain source-to-output records, distinguish actual-item footage from generated context, and review outputs against listing evidence before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ebay-ecommerce-video-generation-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with bash commands and generated video or image files downloaded by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key and may upload selected listing media for remote processing.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
