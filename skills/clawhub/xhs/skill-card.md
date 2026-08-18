## Description:

XHS helps agents plan Xiaohongshu content, draft titles and posts, prepare covers or images, save or publish notes after confirmation, manage creator-center activity, and report visible account metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

External Xiaohongshu creators, content operators, and teams use this skill to create notes, format topics, save drafts, publish after explicit confirmation, reply to comments or messages, and inspect visible creator-center metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft or publish flows may accidentally click the Xiaohongshu publish button while browser automation is controlling a creator account.

Mitigation: Review the publish-button workaround before use and require the agent to stop for explicit confirmation before any click near publish controls.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/mebusw/xhs-browser-ops)
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/xhs)
- [Xiaohongshu Creator Center](https://creator.xiaohongshu.com)
- [Xiaohongshu publish page](https://creator.xiaohongshu.com/publish/publish?from=menu&target=image)
- [Post Templates](references/post-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text summaries with browser-action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports action, account, title, mode, result, details, and next steps; publish actions require explicit user confirmation.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
