## Description: <br>
This skill supports news updates, daily briefings, and world news requests by fetching trusted international RSS feeds and optionally creating voice summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joargp](https://clawhub.ai/user/joargp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to fetch public RSS news feeds, summarize current headlines into concise briefings, and optionally create short voice summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Voice summaries send generated summary text to OpenAI text-to-speech using the user's API key. <br>
Mitigation: Use voice output only for summaries that do not include private or sensitive personal context. <br>
Risk: The skill fetches public news feeds, so summaries depend on the availability and content of external RSS sources. <br>
Mitigation: Review generated summaries and source coverage before relying on them for decisions or redistribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/joargp/skills/news-summary) <br>
- [BBC World RSS feed](https://feeds.bbci.co.uk/news/world/rss.xml) <br>
- [BBC Top Stories RSS feed](https://feeds.bbci.co.uk/news/rss.xml) <br>
- [Reuters world RSS feed](https://www.reutersagency.com/feed/?best-regions=world&post_type=best) <br>
- [NPR News RSS feed](https://feeds.npr.org/1001/rss.xml) <br>
- [Al Jazeera RSS feed](https://www.aljazeera.com/xml/rss/all.xml) <br>
- [OpenAI audio speech API](https://api.openai.com/v1/audio/speech) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, audio, guidance] <br>
**Output Format:** [Markdown or plain text news briefing, with optional shell commands and MP3 audio output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Summaries are typically concise, cover 5-8 top stories, and may cite sources when requested.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
