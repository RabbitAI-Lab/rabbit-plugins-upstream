## Description:

按关键词搜索微信小程序，返回名称、AppID、简介、图标、服务提供方，适合竞品小程序、合作方和小程序调研。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search WeChat mini-programs by keyword and export structured results for market research, partner discovery, or competitor analysis. It requires a trusted ManGeYun API key and user confirmation before paid queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release includes broader API endpoint metadata and an upload helper beyond the advertised mini-program search workflow.

Mitigation: Review the scripts before installation and prefer a narrowed package that removes unrelated endpoints and upload code.

Risk: The local-file upload path can send local files to the external API service when --file or local media paths are used.

Mitigation: Do not pass --file or local file paths unless the API key, destination service, and file contents are trusted and approved.

Risk: The skill requires a paid third-party API key and can trigger billed queries after confirmation.

Mitigation: Confirm the estimate before using --yes, monitor WM_TOTAL_CONSUMPTION and WM_BALANCE, and use only a key intended for this workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-mini-program-finder)
- [ManGeYun API site](https://api.we-media.cn)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands and generated JSON, Markdown, or Excel result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include machine-readable status markers such as WM_OUTPUT_FILE, WM_TOTAL_CONSUMPTION, and WM_BALANCE.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
