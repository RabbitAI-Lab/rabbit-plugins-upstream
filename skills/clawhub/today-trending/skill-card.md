## Description:

Fetches current Weibo, Douyin, and Baidu hot-search rankings and returns agent-friendly JSON for a concise trending-topic summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[php737](https://clawhub.ai/user/php737)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve current Chinese trending topics across Weibo, Douyin, and Baidu, identify cross-platform overlap, and produce a concise Markdown digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes live requests to public Weibo, Douyin, and Baidu endpoints, so network access, endpoint availability, or upstream response changes can affect results.

Mitigation: Run it in an environment where those requests are acceptable and review platform status fields before relying on the generated summary.

Risk: Output is Chinese-first and summarizes fast-changing public trends, which may be incomplete or stale shortly after fetching.

Mitigation: Use the fetched timestamp and source URLs when reviewing time-sensitive topics or sharing results.

Risk: The runtime must provide the needed Python packages and a compatible Python command.

Mitigation: Confirm the Python runtime and dependencies before installing or invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/php737/skills/today-trending)
- [Publisher profile](https://clawhub.ai/user/php737)
- [Weibo hot search](https://weibo.com/hot/search)
- [Baidu realtime hot board](https://top.baidu.com/board?tab=realtime)
- [Douyin hot search endpoint](https://www.iesdouyin.com/web/api/v2/hotsearch/billboard/word/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [JSON from the script followed by a human-facing Markdown summary rendered by the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and runtime access to public Weibo, Douyin, and Baidu endpoints; failed platforms return empty lists while other platforms can still succeed.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
