## Description:

Helps developers build, debug, preview, publish, and optimize WeChat Mini Programs, including optional CloudBase integration and message-push workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create and maintain WeChat Mini Programs, troubleshoot previews, and prepare uploads. It also guides search optimization, customer-service messaging, and CloudBase integration when relevant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned cloud-management packages can change after review.

Mitigation: Use pinned, reviewed local installations of mcporter and CloudBase MCP rather than floating npx or @latest commands.

Risk: Uploads, deployments, message-push changes, and cloud writes can affect live resources.

Mitigation: Require explicit user confirmation before each upload, deployment, message-push mode change, or cloud write.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](artifact/references/message-push-customer-service.md)
- [Mini Program Search Optimization](artifact/references/seo-search-optimization.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide IDE previews, uploads, deployments, and cloud configuration when requested.]

## Skill Version(s):

1.28.65 (source: ClawHub release metadata; bundled frontmatter says 2.34.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
