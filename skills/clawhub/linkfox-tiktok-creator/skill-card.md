## Description:

TikTok 达人（Creator/affiliate creator）数据与可购物视频技能，经 LinkFox 网关代理调用 TikTok Shop 达人开放接口，支持达人主页/档案、达人绑定店铺商品、橱窗商品、可购物视频上传/内容预检/发布/状态查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to retrieve TikTok Shop creator profile, shop-product, and showcase-product data and to run supported shoppable-video publishing checks through LinkFox-mediated TikTok creator APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends TikTok creator tokens and LinkFox API keys to LinkFox services.

Mitigation: Install only when the LinkFox services and configured endpoint environment variables are trusted, and keep tokens masked in user-facing output.

Risk: The scripts store raw API responses and onboarding or payment artifacts on disk.

Mitigation: Run the skill in an approved workspace, review saved files under the LinkFox session directory, and avoid retaining sensitive data longer than needed.

Risk: Onboarding commands can guide account signup, token issuance, and paid-plan purchase flows.

Mitigation: Use onboarding and payment commands only after an explicit user request, and confirm plan and payment choices before creating an order.

## Reference(s):

- [TikTok 达人（Creator）API Reference](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-creator)

## Skill Output:

**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance]

**Output Format:** [JSON API responses, saved response files, text summaries, and Markdown-style command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under a LinkFox session data directory; small responses may also be printed inline, large responses are summarized, and repeated calls can use a 24-hour local cache.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
