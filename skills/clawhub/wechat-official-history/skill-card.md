## Description:

Queries WeChat Official Account history, today's posts, account profile data, and article short-link resolution, returning article titles, timestamps, links, and related account records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and users use this skill to look up WeChat Official Account posting history, today's posts, account profiles, and article short links for operations tracking, competitor content review, and historical article search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores or reads a WM_API_KEY locally and sends authenticated requests to api.we-media.cn.

Mitigation: Use a dedicated key with appropriate account controls, store it only in the documented config or environment location, and rotate or revoke it if no longer needed.

Risk: Local file paths passed through --file or local videoUrl/audioUrl values can be uploaded off-device through the API workflow.

Mitigation: Do not pass local file paths unless upload is intended; review the command parameters before execution.

Risk: The release includes broad unused endpoint metadata and Python bytecode, which increases review burden before installation.

Mitigation: Review the package before installing and prefer a release that removes shipped bytecode and narrows endpoints.json to the advertised endpoints.

Risk: Paid API calls may incur usage charges after confirmation.

Mitigation: Use the built-in estimate step and proceed with --yes only after the user confirms the displayed cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-official-history)
- [Publisher profile](https://clawhub.ai/user/dunkong)
- [We-Media API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown, JSON, or Excel result files, with command-line status markers and concise text summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local WM_API_KEY; paid API calls require cost estimation and explicit confirmation before execution.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; skill frontmatter lists v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
