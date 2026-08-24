## Description:

Helps agents create GPT Image 2 advertising image workflows for performance creatives, using audience, claim evidence, offer, CTA, safe-area, and A/B test constraints before generating images through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing operators, ecommerce teams, and agent builders use this skill to produce ad creative prompts and AI Hive image-generation commands for product ads, retargeting creatives, evidence-led visuals, and single-variable A/B image tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key for generation requests.

Mitigation: Use environment variables or the local config file intentionally, keep the config file permissions restricted, and do not share logs or files containing API keys.

Risk: Reference images passed with --image or --file are uploaded to AI Hive.

Mitigation: Review selected inputs before upload and avoid passing sensitive, private, or unlicensed local files.

Risk: Generated ad images may imply unsupported product claims, prices, certifications, or platform-policy compliance.

Mitigation: Keep claims tied to approved source material, add legal and pricing text after generation from approved sources, and review final creatives against the target ad platform rules.

Risk: Generated files are downloaded to a local output directory.

Mitigation: Confirm the output directory before running tasks and review generated files before reuse or distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-ad-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples, JSON configuration, task-status JSON, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports reference-image uploads, batch generation, routing mode selection, model parameters, task polling, and a configurable output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
