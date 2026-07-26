## Description: <br>
Helps agents retrieve and summarize Douyin creator works, image/text posts, short-drama series, and recent publishing activity using SocialDataX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to inspect Douyin creator content lists and short-drama series for content research, creator benchmarking, recent publishing review, and account tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unbounded pagination with --all can trigger large data pulls or unexpected API usage. <br>
Mitigation: Use bounded options such as --max-items, --pages, or --since-days unless complete retrieval is explicitly needed. <br>
Risk: The skill uses a user-provided SocialDataX API key at runtime. <br>
Mitigation: Provide SOCIALDATAX_API_KEY through the environment only when intending to use SocialDataX; do not store API keys in skill files. <br>


## Reference(s): <br>
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; SocialDataX data calls return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and supports bounded pagination options such as --max-items, --pages, and --since-days.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
