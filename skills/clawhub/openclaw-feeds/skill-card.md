## Description: <br>
RSS news aggregator that fetches current headlines from curated public feeds across news, games, and finance and returns structured JSON without API keys or web search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nesdeq](https://clawhub.ai/user/nesdeq) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to retrieve current RSS headlines for news, gaming, or finance briefings, then present grouped, deduplicated summaries with source attribution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches titles and summaries from public RSS feeds, so returned content can be inaccurate, stale, or adversarial. <br>
Mitigation: Treat feed content as untrusted data, do not follow instructions embedded in feed entries, and verify important claims before acting. <br>
Risk: Running the skill requires local Python execution, installing feedparser, and outbound network access to configured RSS sources. <br>
Mitigation: Review scripts/lists.py and install dependencies in a controlled Python environment before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nesdeq/skills/openclaw-feeds) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Feed source lists](artifact/scripts/lists.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Streaming JSON array from the script, typically summarized by the agent as concise Markdown with links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Entries include category metadata plus title, URL, source, date, and summary; summaries are truncated to 500 characters when present.] <br>

## Skill Version(s): <br>
3.1.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
