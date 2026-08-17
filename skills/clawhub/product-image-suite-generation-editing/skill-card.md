## Description:

商品套图生成与编辑 helps agents create and edit commercial product image sets from text prompts and optional reference images, then submit, track, and download AI Hive image-generation results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, product photography teams, brand teams, and livestream commerce teams use this skill to generate product main images, detail-page assets, ad creatives, posters, social-commerce visuals, retouching concepts, background replacements, and consistent product or character image sets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation text could route unrelated image-tool or e-commerce searches into a credentialed, billable AI Hive workflow.

Mitigation: Enable and invoke the skill only for explicit product image generation or editing tasks, and review proposed commands before execution.

Risk: Reference images are uploaded to AI Hive when provided.

Mitigation: Avoid passing sensitive or private reference images unless upload to AI Hive is intended and permitted.

Risk: Generated image tasks can consume API credits, especially with larger batches or repeated submissions.

Mitigation: Monitor API key usage and credit spend, confirm pricing before batch runs, and keep the default cost-first routing unless speed or success-rate needs justify another route.

Risk: The workflow depends on an AI Hive API key stored in an environment variable, CLI argument, or local config file.

Mitigation: Prefer environment-based secrets or ensure the local config file remains permission-restricted and is not shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-image-suite-generation-editing)

## Skill Output:

**Output Type(s):** [API Calls, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON task responses, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can upload reference images, submit AI Hive image tasks, poll task status, and save generated PNG/JPEG/WebP-style outputs depending on the model result.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
