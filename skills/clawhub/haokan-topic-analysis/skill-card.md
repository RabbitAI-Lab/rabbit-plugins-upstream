## Description:

当用户需要做好看视频选题、短视频内容方向规划或竞品角度复盘时使用。基于用户提供的主题或视频链接，整理相关作品、标题角度与评论反馈，输出带样本依据的选题清单。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者与短视频运营人员可根据主题、受众或好看视频链接，整理候选选题、内容角度和参考标题，并依据可见作品与评论样本复盘竞品方向。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research inputs are sent to SocialDataX and may consume service credits.

Mitigation: Use inputs the user is authorized to submit, and avoid sending sensitive information; check sample scope before expanding requests.

Risk: The skill relies on a SocialDataX API key, and its downloadable CLI was outside the supplied security review.

Mitigation: Keep a dedicated key in the client’s supported secret or environment configuration, never in chat or version control, and prefer a reviewed, pinned CLI version with limited access to unrelated files and secrets.

## Reference(s):

- [SocialDataX API and key management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown topic shortlist with sample evidence and source video links or IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates hot-search clues, video facts, comment feedback, and analysis; notes sample size and missing information; does not promise virality or platform-wide representativeness.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
