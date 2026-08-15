## Description:

Sales Copy Artisan helps agents produce sales copy by extracting FAB selling points, applying emotional hooks, adapting copy for common marketing platforms, and adding CTA language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce sellers, and content teams use this skill to generate structured sales copy for product pages, livestream promotion, social media posts, product launches, and promotions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests shell execution even though its copywriting workflow is mostly documentation-only.

Mitigation: Review before installing, run it only in a constrained agent environment, and prefer a version that removes exec/read permissions unless those capabilities are actually required.

Risk: Generic API, file, and command guidance may lead users to grant unnecessary access for a marketing-copy task.

Mitigation: Limit the skill to copywriting inputs, keep credentials in environment variables, and avoid exposing secrets or unnecessary files to the agent session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sales-copy-artisan)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or JSON-style structured text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces FAB selling points, emotional hook text, platform-adapted copy, CTA text, and warnings for unsupported or missing inputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
