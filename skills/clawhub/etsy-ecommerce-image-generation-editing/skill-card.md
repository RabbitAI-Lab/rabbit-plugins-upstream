## Description:

Create and edit Etsy listing images for handmade, vintage and personalized products, including scale, material, maker-process, customization and gift-packaging visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External Etsy sellers and marketplace operators use this skill to create listing visuals for handmade, vintage, personalized, process, scale, packaging, and shop presentation scenarios while preserving seller-provided product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected listing images, reference files, and prompts are sent to AI Hive for generation.

Mitigation: Use only files intended for the listing workflow, avoid unrelated private files, and review provider account and billing implications before submitting tasks.

Risk: The skill stores and reads an AI Hive API key locally or from the environment.

Mitigation: Prefer least-privilege API keys, keep local configuration restricted, and rotate or revoke keys if exposure is suspected.

Risk: Generated listing images could misrepresent product materials, dimensions, personalization, handmade process, vintage wear, or intellectual-property rights.

Mitigation: Verify seller-provided facts and permissions before publication, and confirm personalized previews before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/etsy-ecommerce-image-generation-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples and JSON task output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may submit AI Hive image-generation tasks and download generated image files to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact CHANGELOG top entry says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
