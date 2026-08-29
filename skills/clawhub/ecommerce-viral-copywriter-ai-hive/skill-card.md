## Description:

Helps ecommerce operators, ad buyers, livestream teams, and content editors turn product facts, audience pain points, proof, platform constraints, tone, and prohibited language into ranked selling points, viral-style titles, short-video scripts, hero-image copy, product-detail copy, CTAs, and optional AI-HIVE image or video generation tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and marketing teams use this skill to create Chinese product copy and campaign production plans from a verified fact base, with optional AI-HIVE commands for image and video assets. It is intended for original, rights-cleared ecommerce content rather than copying protected work, fabricating claims, or bypassing platform rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur billable API use.

Mitigation: Review prompts, model mode, routing, and price snapshots before submitting image or video generation tasks; start with a small sample before batch runs.

Risk: Uploaded reference assets may include material the user is not authorized to use.

Mitigation: Use only rights-cleared images, videos, logos, copy, and reference links; if rights are unclear, keep output to abstract structure guidance and new creative concepts.

Risk: API keys can be exposed if stored carelessly.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable, do not paste real keys into prompts or committed files, and review local configuration permissions.

Risk: Generated ecommerce claims may be misleading if source facts are incomplete or unverified.

Mitigation: Ground selling points, product effects, pricing, inventory, scale, and endorsements in supplied evidence, and avoid guarantees about sales, traffic, ranking, review approval, or return on investment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ecommerce-viral-copywriter-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured sections, JSON production briefs, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task records such as routing mode, model, pricing snapshot, taskId, status, and downloaded file locations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
