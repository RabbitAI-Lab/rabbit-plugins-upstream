## Description: <br>
Daily Hot News helps agents query, aggregate, summarize, personalize, and monitor hot-topic lists from 54 public platforms through a local DailyHotApi service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[one-box-u](https://clawhub.ai/user/one-box-u) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers and agent users use this skill to retrieve current public hot-news rankings, browse supported sources, build cross-platform summaries, save local history, and configure personalized or monitored topic views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a separate DailyHotApi backend for public hot-news aggregation. <br>
Mitigation: Review and trust the DailyHotApi backend before running it, and point DAILY_HOT_API_URL only at the intended local service. <br>
Risk: Local history and personalized preferences can retain queried topics, keywords, and platform choices. <br>
Mitigation: Set DAILY_HOT_AUTO_SAVE=false if local history is not wanted, review the configured data directory, and clear old saved data as needed. <br>
Risk: Optional scheduled or Feishu push behavior can send hot-list content to an unintended destination. <br>
Mitigation: Enable push behavior only after confirming credentials, destination, schedule, and the process for disabling notifications. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/one-box-u/skills/daily-hot-news) <br>
- [DailyHotApi](https://github.com/imsyy/DailyHotApi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown-formatted text with hot-list results, source lists, status messages, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, requests, aiohttp, and a trusted local DailyHotApi service; may save local history and personalized settings when enabled.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
