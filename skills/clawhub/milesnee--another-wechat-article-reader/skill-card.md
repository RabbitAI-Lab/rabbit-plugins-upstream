## Description:

Reads public WeChat article URLs from mp.weixin.qq.com with local scripts and returns structured article data, including title, publication time, author, and body text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[milesnee](https://clawhub.ai/user/milesnee)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill when they need to fetch and parse public WeChat articles into structured JSON instead of relying on generic web fetch or search behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local HTTP-fetch scripts against network URLs.

Mitigation: Use it only for public mp.weixin.qq.com article URLs and review the fetched result before relying on it.

Risk: The diagnostic fallback script can fetch arbitrary hosts and has weaker URL scoping than the main script.

Mitigation: Prefer the main reader script and avoid the diagnostic fallback on arbitrary URLs until host validation and redirect handling are tightened.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/milesnee/skills/another-wechat-article-reader)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON containing article metadata, plain-text content, source URL, extraction method, strategy, and execution logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The main script accepts a public mp.weixin.qq.com article URL plus optional timeout, retry count, and retry delay parameters.]

## Skill Version(s):

0.3.0 (source: server release evidence and SKILL.md frontmatter; pyproject.toml and _meta.json list 0.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
