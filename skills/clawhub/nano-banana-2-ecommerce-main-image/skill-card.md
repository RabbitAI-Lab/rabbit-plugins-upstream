## Description:

Uses Nano Banana 2 through AI Hive to create readable, channel-aware ecommerce product main images and platform-specific test variants from approved product references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce operators, marketers, and product-listing teams use this skill to generate product main-image candidates for marketplaces and content-commerce channels while preserving SKU facts, safe crop zones, and thumbnail readability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and generated outputs may contain commercially sensitive product details.

Mitigation: Use only approved product images and confirm that uploading them to AI Hive or its returned object-storage URL is permitted.

Risk: Running init may store an API key in the user's home directory.

Mitigation: Prefer environment-variable or command-line key injection when appropriate, and keep any saved configuration restricted to owner-only permissions.

Risk: Generated ecommerce images may imply unsupported product claims or violate channel-specific listing rules.

Mitigation: Review each output against current marketplace rules and verified SKU facts before publication.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/nano-banana-2-ecommerce-main-image)
- [AI Hive API endpoint referenced by the skill](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page referenced by the skill](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls, files]

**Output Format:** [Markdown instructions with inline bash commands; generated image files are downloaded locally by the helper script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana 2 image model through AI Hive, accepts optional reference images, supports batch generation and routing modes, and can query existing task IDs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
