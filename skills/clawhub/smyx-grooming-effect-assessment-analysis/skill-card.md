## Description:

Assesses post-grooming pet images or videos for remaining mats, dandruff coverage, and coat smoothness, then returns a grooming score and suggested follow-up care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet owners, and grooming service operators use this skill to evaluate grooming quality from pet media, check for remaining mats or dandruff, and decide whether additional grooming or care is warranted. The results are visual assessments only and are not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, and analysis requests are sent to lifeemergence.com services.

Mitigation: Use only media that is appropriate to send to that service, and avoid submitting sensitive or unnecessary background content.

Risk: The skill can silently create or reuse a cloud-linked identity and associate report history with it.

Mitigation: Review the identity behavior before installation and use an environment where this account linkage is acceptable.

Risk: Reusable backend tokens or identity values may be stored locally in the workspace data directory.

Mitigation: Review or remove existing data/smyx-api-key.txt and workspace data before use if that identity should not be reused.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown report text with structured JSON content, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local or URL media input; local files are limited to supported formats and a 10 MB maximum.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
