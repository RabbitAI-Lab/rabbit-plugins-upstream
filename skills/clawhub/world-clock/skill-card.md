## Description: <br>
Answers time and timezone questions with live data from the worldclock.pro MCP server, including city and country time, timezone conversion, DST clock-change dates, UTC or GMT offsets, coordinate lookup, and multilingual city search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alex-hey-alex](https://clawhub.ai/user/alex-hey-alex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs current time facts, timezone conversions, daylight-saving transitions, UTC offsets, or city timezone resolution without relying on stale memorized timezone rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Time, scheduling, and location queries may be sent to worldclock.pro. <br>
Mitigation: Avoid including confidential meeting details or sensitive personal locations unless sharing them with the service is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alex-hey-alex/skills/world-clock) <br>
- [World Clock Pro homepage](https://worldclock.pro) <br>
- [World Clock Pro MCP endpoint](https://worldclock.pro/mcp) <br>
- [World Clock Pro agent page map](https://worldclock.pro/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown, shell commands] <br>
**Output Format:** [Markdown text with time facts, source links, and optional curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live worldclock.pro responses; results may include ISO timestamps, local date and time, weekday, UTC offset, abbreviation, zone name, DST state, and source_url.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
