## Description:

当用户需要做抖音选题、抖音内容选题、短视频选题策划、爆款角度拆解、内容方向规划或选题素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, brand researchers, creators, and their agents use this skill to retrieve read-only Douyin search or hot-list data and organize topic ideas, source examples, and follow-up analysis angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the SocialDataX npm package and sends requests using the user's SOCIALDATAX_API_KEY.

Mitigation: Confirm trust in the SocialDataX package and service before installation or execution, and keep the API key in the environment rather than embedding it in generated files.

Risk: Douyin results can be incomplete, paginated, filtered, unavailable, or time-sensitive, which can lead to misleading topic conclusions if treated as exhaustive.

Mitigation: Separate visible evidence from analysis, preserve traceable result fields and pagination tokens, and broaden or retry focused queries when results are sparse or calls fail.

Risk: Insufficient balance or local Node.js/npm/network issues can interrupt retrieval.

Mitigation: Preserve any partial results, avoid repeated retries on insufficient_balance, and resolve the API key, account balance, network, or local runtime issue before continuing the same command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-topic-analysis)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON result interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY with Node.js/npm; retrieves read-only Douyin search and hot-list data and preserves traceable IDs, links, titles, authors, metrics, publish times, content types, and pagination tokens when relevant.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
