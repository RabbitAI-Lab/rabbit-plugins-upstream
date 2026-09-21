## Description:

Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intelligent pet butlers. | 宠物品种个体识别技能，精准识别猫狗宠物品种，支持多宠家庭区分不同独立个体，智能宠物管家好帮手

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze pet images or videos, identify cat and dog breeds, distinguish individual pets in multi-pet scenes, and list prior pet analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images/videos, generated or reused identity, report history, and locally stored tokens may be sent to configured external services.

Mitigation: Review service endpoints and obtain explicit user consent for identity creation, token persistence, media upload, and history retrieval before installation or use.

Risk: The security evidence reports active plaintext HTTP endpoints despite HTTPS protection claims.

Mitigation: Use HTTPS-only production endpoints and remove or disable plaintext HTTP configuration before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet breed individual recognition API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text and JSON results, with Markdown tables or report links when report history is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet counts, breed and individual identification results, confidence values, remarks, report links, and historical report lists.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
