## Description: <br>
Read transcripts and summaries from Pocket AI recording devices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmustier](https://clawhub.ai/user/tmustier) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to retrieve, search, and analyze their own Pocket AI recordings, transcripts, summaries, and action items from a logged-in Pocket account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill extracts and stores a Firebase bearer token from the user's logged-in Pocket browser session at ~/.pocket_token.json. <br>
Mitigation: Install only when comfortable granting that access, treat the token file like a password, remove it when not needed, and avoid using the skill on shared machines. <br>
Risk: Transcript, summary, speaker, action item, and recording metadata outputs may contain private conversation data. <br>
Mitigation: Keep outputs out of public channels, repositories, logs, and backups unless the user has explicitly reviewed and approved the content. <br>
Risk: The integration uses a reverse-engineered unofficial Pocket API and may fail or return unexpected data if Pocket changes its web app or endpoints. <br>
Mitigation: Review results before relying on them and re-check authentication or API behavior when errors or missing fields appear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tmustier/skills/heypocket-reader) <br>
- [Pocket AI](https://heypocket.com) <br>
- [Pocket web app](https://app.heypocket.com) <br>
- [Pocket API base endpoint](https://production.heypocketai.com/api/v1) <br>
- [Anthropic browser skill](https://github.com/anthropics/skills/tree/main/skills/browser) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, transcript text, markdown summaries, and action item lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include private recording metadata, transcripts, summaries, speakers, action items, tags, and optional location fields returned by Pocket.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
