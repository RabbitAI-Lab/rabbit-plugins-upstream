## Description:

用于抖音达人数据、抖音达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Douyin creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve read-only Douyin creator profile data through SocialDataX with a configured API key. It supports reporting available profile facts such as names, platform IDs, bios, verification, audience counts, IP location, and gender while keeping factual results separate from strategic interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key and sends lookup parameters through the SocialDataX CLI or MCP integration.

Mitigation: Install and use it only when the publisher and SocialDataX are trusted, and avoid running it in environments where unrelated secrets are exposed unnecessarily.

Risk: The documented examples use npx with the latest npm package.

Mitigation: Apply normal package-source caution, and pin or verify the package version when stronger supply-chain control is required.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-profile)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY; read-only Douyin creator profile lookup via SocialDataX.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
