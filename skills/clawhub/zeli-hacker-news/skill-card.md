## Description: <br>
Read Hacker News with AI summaries in the user's language via zeli.app, including daily front-page digests as markdown or JSON, permanent story summary pages, and RSS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mazzzystar](https://clawhub.ai/user/mazzzystar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to retrieve and summarize Hacker News front-page coverage for daily technology briefings, topic checks, and non-English readers. It is intended for users who want concise HN highlights with links back to original articles, HN discussions, and Zeli summary pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AI-generated story summaries can omit nuance or be incorrect. <br>
Mitigation: Use the provided original article and Hacker News discussion links to verify important details before relying on a summary. <br>
Risk: Briefings depend on availability and freshness of external Zeli endpoints. <br>
Mitigation: Cache dated digests when possible and handle fetch failures or stale responses gracefully. <br>


## Reference(s): <br>
- [Zeli](https://zeli.app) <br>
- [Zeli LLM context](https://zeli.app/llms.txt) <br>
- [Canonical Zeli skill](https://zeli.app/skill.md) <br>
- [ClawHub listing](https://clawhub.ai/mazzzystar/skills/zeli-hacker-news) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown or JSON fetched from Zeli endpoints, with links to original articles, HN discussions, and summary pages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports 30 language codes, hourly daily digest updates, immutable dated digests, and unauthenticated access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
