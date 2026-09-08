## Description:

Finds and dissects benchmark creators on Douyin, Xiaohongshu, or WeChat Channels by screening monetization, comprehensibility, and copyability, then guiding extraction of early, top-engagement, and latest posts into a teardown and adaptation roadmap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to identify a suitable benchmark creator, evaluate whether that creator is worth learning from, and structure a detailed content teardown before adapting ideas into their own work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require paid TikHub API calls and may create costs while scraping third-party platforms.

Mitigation: Review cost estimates before running paid requests, use dry-run steps where available, and stop if the expected request volume is unclear.

Risk: The workflow references a broad TikHub API key and insecure storage or sharing of credentials could expose paid API access.

Mitigation: Use a scoped and revocable key where possible, store it in a secure credential store, and avoid pasting secrets into chat or shell history.

Risk: The workflow can collect third-party creator content, transcripts, covers, and local records that may include private or copyrighted material.

Mitigation: Use collected content only for private analysis, avoid republishing copied content, and delete local records that are no longer needed.

Risk: Persistent or shared memory may retain benchmarking details without clear user controls.

Mitigation: Review what is written to local memory, avoid saving sensitive account or creator information, and remove stored records when they are not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-benchmark)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [三筛判据](references/三筛判据.md)
- [抓取手册](references/抓取手册.md)
- [规则卡](references/规则卡.md)
- [TikHub](https://tikhub.io)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown reports and tables with shell commands, CSV-style content lists, local file paths, and optional configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may produce a full post list, three selected content batches, media metadata, transcripts when available, and a final teardown and adaptation plan.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
