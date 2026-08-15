## Description:

当用户需要做抖音内容研究、抖音选题、热点观察、竞品内容对比、趋势判断或素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators use this skill to inspect Douyin hot searches, compare competitor content, evaluate topic trends, and organize traceable content samples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, pagination tokens, and the SocialDataX API key to the hosted SocialDataX service.

Mitigation: Install only if that data flow is acceptable for the intended use, and avoid entering sensitive research terms when policy requires local-only handling.

Risk: The artifact examples use the npm package with @latest, which can change over time.

Mitigation: For stricter supply-chain control, review or pin the SocialDataX npm package version before deployment.

## Reference(s):

- [SocialDataX API key and CLI homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-content-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and SOCIALDATAX_API_KEY; SocialDataX CLI responses return Douyin hot-search or search result data.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
