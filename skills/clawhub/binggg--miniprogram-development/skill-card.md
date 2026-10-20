## Description:

Guides agents through building, debugging, previewing, publishing, and optimizing WeChat Mini Programs, with optional CloudBase integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to build and troubleshoot WeChat Mini Program pages and configuration, preview and upload releases, and handle search, messaging, and CloudBase integration when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned cloud-tool commands may run unexpected package versions during authentication or cloud operations.

Mitigation: Review commands and pin and verify package versions before running npx tools.

Risk: Preview, upload, cloud-function deployment, and message-push configuration can affect live projects.

Mitigation: Test in a non-production CloudBase environment and confirm the target project and environment before deployment or configuration changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/binggg/skills/miniprogram-development)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [DevTools debugging and preview](artifact/references/devtools-debug-preview.md)
- [CloudBase integration](artifact/references/cloudbase-integration.md)
- [Message push and customer service](artifact/references/message-push-customer-service.md)
- [Mini Program search optimization](artifact/references/seo-search-optimization.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project configuration, preview and upload steps, and CloudBase integration guidance.]

## Skill Version(s):

1.28.91 (source: ClawHub release; artifact frontmatter: 2.36.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
