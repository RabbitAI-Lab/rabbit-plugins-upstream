## Description:

按 B 站用户主页链接查询 UP 主的账号资料及关注、粉丝、获赞和播放数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Bilibili creators, marketers, and analysts use this skill to look up an UP creator's public profile and engagement counts from a supplied profile link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install Node/npm tooling and change user-level PATH configuration.

Mitigation: Review environment changes before installation; prefer a preinstalled or pinned qhkit version.

Risk: The skill may store a qhkit API token or accept an optional Bilibili session cookie.

Mitigation: Review credential storage and avoid supplying a Bilibili cookie unless session access is understood and needed.

Risk: Creator lookups use paid calls with charges that may vary by result size.

Mitigation: Check the current estimate and obtain explicit approval before paid calls, especially bulk requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-bilibili-creator-profile)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise natural-language answer with creator metrics; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports paid-call credits and may include a small data preview.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
