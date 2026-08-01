## Description: <br>
Answers time and timezone questions with live data from the worldclock.pro MCP server, including city and country times, timezone conversion, meeting scheduling across time zones, daylight saving changes, UTC/GMT offsets, coordinate-based timezone lookup, and city resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldclock.pro](https://clawhub.ai/user/worldclock.pro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer current time, timezone conversion, daylight saving, UTC offset, coordinate timezone, and city-resolution questions using live data from worldclock.pro. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Timezone questions may be sent to worldclock.pro over the network. <br>
Mitigation: Use the skill only when sending the requested place, timezone, coordinate, or conversion details to worldclock.pro is acceptable. <br>
Risk: Time and timezone answers can be wrong if the MCP server is unavailable and the agent falls back to memory. <br>
Mitigation: Use the provided worldclock.pro MCP endpoint, curl fallback, or listed server-rendered pages; avoid answering timezone questions from memory. <br>


## Reference(s): <br>
- [WorldClock.pro](https://worldclock.pro) <br>
- [WorldClock.pro MCP endpoint](https://worldclock.pro/mcp) <br>
- [WorldClock.pro agent page map](https://worldclock.pro/llms.txt) <br>
- [WorldClock.pro London city page](https://worldclock.pro/en/city/london) <br>
- [WorldClock.pro London to Tokyo converter](https://worldclock.pro/en/convert/london-to-tokyo) <br>
- [WorldClock.pro EST timezone reference](https://worldclock.pro/en/timezone/est) <br>
- [ClawHub skill page](https://clawhub.ai/worldclock.pro/skills/world-clock-pro) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/worldclock.pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text answers with optional JSON-RPC curl commands and linked source URLs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool responses include time fields such as iso, date, time, time12, weekday, utcOffset, abbreviation, zoneName, isDST, and source_url when available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
