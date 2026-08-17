## Description:

This skill helps agents search SHEIN for visually similar products from a supplied image through GeekBI, then summarize candidate matches, market signals, pricing, sales, ratings, launch timing, and competition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace analysts, and sourcing teams use this skill to find visually similar SHEIN products from product photos, screenshots, supplier images, image URLs, or encoded images. It supports candidate filtering and business analysis for visual matches, price bands, sales performance, competition, and follow-up validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images are uploaded to GeekBI for visual search.

Mitigation: Use only images that are appropriate to share with GeekBI, and avoid submitting confidential product imagery unless that sharing is approved.

Risk: The security review reports reused login state through a mismatched Temu-named auth path.

Mitigation: Review the auth-state behavior before installation, especially on machines that also use other GeekBI or Temu-related skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-image-search-skill)
- [Server-resolved source repository](https://github.com/geekbi/geekbi-shein-image-search-skill)
- [SHEIN image search workflow](references/SHEIN图搜同款.md)
- [SHEIN image search interface](references/SHEIN图搜同款接口.md)
- [Query pause and resume process](references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown analysis with linked product titles and concise evidence-based findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include site, filter, pagination, and data-freshness context; avoids exposing image encodings or raw JSON unless requested for troubleshooting.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
