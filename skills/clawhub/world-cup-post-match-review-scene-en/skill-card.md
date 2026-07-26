## Description: <br>
Used to generate post-match reviews of World Cup football matches, with standardized scene input, post-match information retrieval, and fan group notification extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and football community managers use this skill to create concise World Cup match summaries, match analysis, best-player highlights, and post-match talking points for sharing in fan chats or community updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may query local notifications broadly when generating fan discussion or hot-topic sections. <br>
Mitigation: Configure specific apps, groups, and a narrow time window before using notification-backed hot-topic or full-review modes. <br>
Risk: Notification content can include unrelated or sensitive personal messages. <br>
Mitigation: Use only short, match-relevant snippets and omit irrelevant notification categories from the generated review. <br>
Risk: Live or unfinished matches can lead to premature final-score or post-match conclusions. <br>
Mitigation: Confirm match status first and use real-time or pre-game wording until an official full-time result is available. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown post-match review, real-time result, or pre-game overview depending on match status] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are selected by requested focus: one-sentence summary, match analysis, best performer, hot topics, or full review; Chinese is the default language unless the user requests otherwise.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
