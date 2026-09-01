## Description:

Accurately identifies cat and dog breeds and supports distinguishing between different individuals in multi-pet households; an essential assistant for intelligent pet butlers. | 宠物品种个体识别技能，精准识别猫狗宠物品种，支持多宠家庭区分不同独立个体，智能宠物管家好帮手

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to identify cat or dog breeds, distinguish individual pets in multi-pet households, and retrieve prior pet recognition reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet or household media, report history, and identity metadata to a cloud service.

Mitigation: Use it only when the publisher and cloud service are trusted for that data, and avoid submitting sensitive household footage unless the deployment has approved data-handling terms.

Risk: The skill may create or reuse local identity state and store account tokens in the workspace.

Mitigation: Run it in an isolated workspace, review and clear local state after use, and rotate any exposed or no-longer-needed tokens.

Risk: Security evidence reports insecure development HTTP endpoint defaults despite HTTPS claims.

Mitigation: Before deployment, configure production HTTPS endpoints and verify the active runtime configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown text with structured JSON analysis content, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include pet count, breed assessment, individual distinction results, confidence, notes, and historical report listings.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
