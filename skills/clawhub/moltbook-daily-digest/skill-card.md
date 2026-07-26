## Description: <br>
Get a daily digest of trending posts from Moltbook with Chinese summaries. Uses Google Translate for full Chinese translation of post content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangfugui1799](https://clawhub.ai/user/wangfugui1799) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch trending Moltbook posts and produce a Chinese daily digest with summaries, engagement counts, authors, and links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Moltbook API key to fetch posts. <br>
Mitigation: Set MOLTBOOK_API_KEY directly when possible, keep any credentials file tightly permissioned, and use a least-privileged key if Moltbook supports one. <br>
Risk: Selected Moltbook post text may be sent to Google Translate through deep-translator. <br>
Mitigation: Use the skill only when that translation path is acceptable for the post content being summarized. <br>
Risk: The skill depends on the deep-translator package at runtime. <br>
Mitigation: Consider pinning the dependency version before running the skill. <br>


## Reference(s): <br>
- [Moltbook API Reference](artifact/references/api.md) <br>
- [Moltbook API Base URL](https://www.moltbook.com/api/v1) <br>
- [Moltbook Explore](https://moltbook.com/explore) <br>
- [ClawHub Skill Page](https://clawhub.ai/wangfugui1799/skills/moltbook-daily-digest) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown digest with Chinese summaries, engagement counts, authors, and Moltbook links; setup guidance may include shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Moltbook API key. Selected Moltbook post text may be sent to Google Translate through deep-translator.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, released 2026-02-06) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
