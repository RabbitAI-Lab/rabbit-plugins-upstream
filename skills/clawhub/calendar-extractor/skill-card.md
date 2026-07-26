## Description: <br>
Calendar Extractor reads recent HiJavis audio and keyboard transcripts, extracts likely calendar events, writes them as pending calendar rows, and sends per-event markdown cards to iOS chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samuel-wei](https://clawhub.ai/user/samuel-wei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External HiJavis users use this skill to turn recent conversation and keyboard transcript references to meetings, appointments, and plans into pending calendar entries and chat cards they can confirm, discard, or edit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically analyzes completed voice and keyboard transcript units, which may include private content. <br>
Mitigation: Enable it only when the user accepts this transcript access, and provide controls to disable auto-runs or limit transcript windows. <br>
Risk: Extracted event details can be surfaced without explicit approval for each run. <br>
Mitigation: Keep extracted events pending until the user confirms them, and allow users to discard or edit events before treating them as confirmed. <br>
Risk: Relative or ambiguous time language can produce inaccurate calendar details. <br>
Mitigation: Resolve dates from the fetched local reference date and timezone, and leave unresolved fields null or ask for clarification when the transcript is ambiguous. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/samuel-wei/skills/calendar-extractor) <br>
- [Route Contract](references/route-contract.md) <br>
- [HiJavis iPhone App](https://apps.apple.com/us/app/hijavis/id6745134765) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, API calls, configuration] <br>
**Output Format:** [JSON transcript and anchor payloads, JSON event or update input, per-event Markdown chat cards, and local JSON dedup state.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a 24-hour default transcript window, event-level deduplication, and pending event status until user confirmation.] <br>

## Skill Version(s): <br>
0.7.1 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
