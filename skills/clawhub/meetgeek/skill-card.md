## Description: <br>
Query MeetGeek meeting intelligence from CLI - list meetings, get AI summaries, transcripts, action items, and search across all your calls with natural language. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nexty5870](https://clawhub.ai/user/nexty5870) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and meeting participants use this skill to query MeetGeek from an agent workflow, including listing meetings, retrieving summaries and transcripts, reviewing action items, and searching meeting text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose meeting summaries, transcripts, speaker names, action items, exported files, and other confidential meeting content. <br>
Mitigation: Treat retrieved meeting content as confidential, review outputs before sharing, and avoid saving transcripts or exports in shared or insecure locations. <br>
Risk: The MeetGeek API key is saved locally for CLI access. <br>
Mitigation: Install only when the MeetGeek CLI package is trusted, protect the local configuration file, and clear the saved API key when access is no longer needed. <br>


## Reference(s): <br>
- [meetgeek-cli npm package](https://www.npmjs.com/package/meetgeek-cli) <br>
- [meetgeek-cli GitHub project linked by the skill](https://github.com/nexty5870/meetgeek-cli) <br>
- [ClawHub MeetGeek listing](https://clawhub.ai/nexty5870/skills/meetgeek) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May retrieve or save MeetGeek summaries, transcripts, highlights, action items, and search results.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
