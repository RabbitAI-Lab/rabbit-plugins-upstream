## Description:

Review planned social-media content before publication for legal, platform-policy, account-safety, privacy, copyright, advertising, and audience-safety risks across scripts, captions, titles, comments, images, cover art, video frames, and audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoxiaochen5678-dot](https://clawhub.ai/user/xiaoxiaochen5678-dot)

### License/Terms of Use:

MIT

## Use Case:

External creators, marketers, and content teams use this skill to review planned mainland China social-media content before publication. It identifies legal, platform-policy, account-safety, privacy, copyright, advertising, and audience-safety risks, then gives platform-specific revision guidance.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Users may treat the review as legal advice or a guarantee of platform approval.

Mitigation: Use the output as decision support, keep the skill's boundary notice visible, and require qualified legal or platform review for high-stakes content.

Risk: Private or sensitive publication materials may be submitted for review.

Mitigation: Redact passwords, identity numbers, payment information, account recovery details, private contact details, unpublished customer data, and faces or voices lacking consent before review.

Risk: Platform rules and advertising requirements may change after the bundled rule library was checked.

Mitigation: Verify time-sensitive or high-stakes conclusions against current primary sources before publication, and mark unverifiable rules as requiring confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoxiaochen5678-dot/skills/content-compliance-review-skill)
- [Server-resolved source repository](https://github.com/xiaoxiaochen5678-dot/content-compliance-review-skill)
- [Common cross-platform risks](references/common-risks.md)
- [Platform rule index](references/platforms/index.md)
- [Douyin community rules summary](references/platforms/douyin.md)
- [Douyin minors overlay](references/platforms/douyin-minors.md)
- [Douyin medical overlay](references/platforms/douyin-medical.md)
- [Douyin marketing and generated-content overlay](references/platforms/douyin-marketing.md)
- [Douyin legal-content overlay](references/platforms/douyin-legal.md)
- [Xiaohongshu rules summary](references/platforms/xiaohongshu.md)
- [WeChat Channels rules summary](references/platforms/wechat-channels.md)
- [WeChat Official Accounts rules summary](references/platforms/wechat-official-accounts.md)
- [Mainland China advertising compliance baseline](references/laws/china-advertising.md)
- [Rule library schema](references/rule-schema.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown compliance review report with risk levels, evidence layers, platform differences, unresolved facts, and revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responds in the user's language and labels stale, missing, inaccessible, or conflicting evidence as requiring verification.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
