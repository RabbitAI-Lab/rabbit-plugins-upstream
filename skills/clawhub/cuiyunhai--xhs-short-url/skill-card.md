## Description:

将小红书笔记长链接批量转换为 xhslink.com 短链接，支持异步查询和结果导出。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

需要分享小红书公开笔记的用户和代理可将每批 1–50 条笔记长链接转换为短链接，并查询或导出结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service address sends account tokens over plaintext HTTP.

Mitigation: Use only on a trusted network and configure a verified HTTPS service address before login when available.

Risk: The account token is stored locally and shared with related Xiaohongshu skills.

Mitigation: Protect local configuration access and consider the effect on other skills before changing credentials or logging out.

Risk: Disabling HTTPS certificate verification exposes authenticated requests to interception.

Mitigation: Keep certificate verification enabled and use a service address with a valid certificate.

Risk: The bundled client includes comment-session methods beyond short-link conversion.

Mitigation: Review the package before installation and restrict use to the intended short-link commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cuiyunhai/skills/xhs-short-url)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV files]

**Output Format:** [Short-link URLs in text; JSON command results; optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 50 links per batch; asynchronous results can be polled.]

## Skill Version(s):

1.0.2 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
