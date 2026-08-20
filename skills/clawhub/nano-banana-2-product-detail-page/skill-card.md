## Description:

This skill helps agents plan modular product-detail-page visuals for Nano Banana 2 and generate PDP module backgrounds through AI Hive while preserving product evidence, layout whitespace, and review requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, designers, and developers use this skill to structure PDP and Amazon A+ modules, then generate reference-grounded visual backgrounds for ecommerce product pages. It is suited for workflows that require approved product assets, evidence-backed claims, and final human layout review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for image generation.

Mitigation: Use approved product assets only, avoid private or unauthorized images, and review whether the AI Hive processing path is acceptable for the intended release.

Risk: The skill can store an AI Hive API key in a local configuration file.

Mitigation: Use a scoped API key where possible, keep local file permissions restricted, and rotate the key if it may have been exposed.

Risk: Generated PDP visuals may imply unsupported product claims, certifications, comparisons, or platform affiliations.

Mitigation: Keep claims, ratings, compliance statements, and platform references backed by approved evidence and perform final human review before publication.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples, JSON task status, and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are downloaded locally by default; API keys can be supplied by command line, environment variable, or local configuration.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
