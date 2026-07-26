## Description: <br>
用于快手达人数据、快手达人作品、作品列表、近期发布、内容调研和创作者内容分析，覆盖 Kuaishou / Kwai creator works，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, and marketing analysts use this skill to retrieve and summarize Kuaishou / Kwai creator video lists for content research, recent publishing review, account tracking, and creator benchmarking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses SOCIALDATAX_API_KEY with the SocialDataX CLI/API. <br>
Mitigation: Use it only when you intend to provide that API key to SocialDataX, keep the key in the environment, and avoid embedding it in prompts or files. <br>
Risk: Unbounded pagination can cause large API usage. <br>
Mitigation: Prefer --max-items, --pages, or --since-days for cost control, and avoid --all unless the user explicitly wants a complete crawl. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-videos) <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Kuaishou creator work-list retrieval; pagination can be bounded with --pages, --max-items, or --since-days.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
