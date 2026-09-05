## Description:

Guides agents through creating ecommerce livestream avatar videos with DLazy, including base-portrait recipes and a script, TTS, avatar, B-roll, and assembly pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing teams use this skill to plan and produce product-selling avatar videos for TikTok Shop, Douyin, Amazon, Shopee, and brand stores. It is most useful when an agent needs reusable avatar recipes, segmented spoken scripts, DLazy CLI commands, and production troubleshooting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends ecommerce prompts and media to DLazy services.

Mitigation: Use the skill only when DLazy is trusted for the project and avoid sensitive product assets unless upload is acceptable.

Risk: The workflow can incur paid generation costs.

Mitigation: Run dry-run checks before paid generation and segment scripts to avoid rejected requests caused by prompt or duration limits.

Risk: The DLazy API key may be stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the local config and environment variable, and avoid exposing credentials in shared logs, prompts, or generated files.

Risk: Avatar product videos may trigger advertising, AI-disclosure, or platform policy requirements.

Mitigation: Review product claims, avoid unsupported or absolute claims, and follow platform rules for AI-generated-content disclosure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-avatar)
- [DLazy homepage](https://dlazy.com)
- [Pipeline guide](artifact/pipeline.md)
- [Base portrait recipes](artifact/recipes.md)
- [Troubleshooting and compliance notes](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for DLazy CLI workflows; generated media and paid service calls are performed by DLazy, not by the skill text itself.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
