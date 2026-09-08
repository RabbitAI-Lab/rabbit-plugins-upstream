## Description:

OpenLX 微信公众号免白名单发布 authorizes a WeChat Official Account and routes prepared article, image, authorized reprint, video, or audio operations through the OpenLX gateway without generating content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlxcn](https://clawhub.ai/user/openlxcn)

### License/Terms of Use:

MIT

## Use Case:

External developers and operators managing WeChat Official Accounts use this skill to hand prepared publishing or media-upload requests to OpenLX, avoid repeated client-IP allowlist changes, and query the original operation status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure or overbroad account authority when using the OpenLX API key.

Mitigation: Use a limited OpenLX API key, provide credentials only through OPENLX_WEIXIN_API_KEY or an existing secure store, and avoid placing credentials in requests, examples, logs, or skill files.

Risk: Installer and updater operations can replace local agent skill directories.

Mitigation: Review the package before installing, avoid unattended update flags unless replacement is intended, keep local-change backups, and verify package hashes before accepting updates.

Risk: A write operation may have an uncertain result after a timeout or gateway error.

Mitigation: Do not blindly retry writes; query the original media_id or publish_id and report SUBMITTED_UNVERIFIED when status cannot be confirmed.

Risk: Update metadata is not signed or host-pinned according to the security evidence.

Mitigation: Prefer signed or host-pinned update metadata before broad deployment, and use only trusted official sources while reviewing redirects and package hashes.

## Reference(s):

- [OpenLX skill homepage](https://wx.openlx.cn/skills/openlx-weixin-baimindan)
- [ClawHub skill page](https://clawhub.ai/openlxcn/skills/openlx-weixin-baimindan)
- [Authorization](references/AUTHORIZATION.md)
- [Handoff Contract](references/HANDOFF_CONTRACT.md)
- [Security and Privacy](references/SECURITY_AND_PRIVACY.md)
- [Installation](references/INSTALL.md)
- [Update and Rollback](references/UPDATE.md)
- [Troubleshooting](references/TROUBLESHOOTING.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON handoff examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes prepared requests only; it does not write, edit, generate, or transform publication content.]

## Skill Version(s):

0.1.1 (source: SKILL.md metadata, VERSION file, and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
