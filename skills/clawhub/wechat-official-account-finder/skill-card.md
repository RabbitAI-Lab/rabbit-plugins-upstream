## Description:

按关键词搜索微信公众号账号并返回名称、简介、微信号、认证主体，也可查看公众号资料。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and content researchers use this skill to find WeChat official accounts by keyword or industry and inspect account profile details for benchmarking, partnership discovery, or sector research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports under-disclosed local file upload code and broader API metadata than the advertised account lookup purpose needs.

Mitigation: Review the skill before installing, avoid `--file` and local media-path parameters, and prefer a release that removes unused upload code and unnecessary endpoint inventory.

Risk: The skill requires a provider API key and sends lookup queries and returned data through the provider service.

Mitigation: Use it only when the provider is trusted with the API key and query results, and keep `config.json` out of shared folders and repositories.

Risk: The release includes shipped Python bytecode files in addition to source files.

Mitigation: Prefer a source-only release or inspect the bytecode files during review before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-official-account-finder)
- [We-Media API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and a We-Media API key; paid API calls require explicit confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter lists v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
