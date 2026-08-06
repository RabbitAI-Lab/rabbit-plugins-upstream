## Description: <br>
Calendar Extractor scans recent recording and keyboard transcripts to identify calendar events, write them as pending HiJavis calendar records, and push one markdown card per event to iOS chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samuel-wei](https://clawhub.ai/user/samuel-wei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External HiJavis users use this skill to turn recent spoken or typed scheduling mentions into reviewable calendar event cards. Agents use it to fetch transcript context, extract structured event fields, push markdown cards, and update pending calendar rows when users correct details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automatically receives and processes sensitive completed voice and keyboard transcript units. <br>
Mitigation: Enable it only where users accept that transcript processing, and review HiJavis privacy controls, transcript retention, scheduled-summary settings, and disable controls before use. <br>
Risk: Automatic extraction can create calendar records or chat cards from scheduling language before a user explicitly asks each time. <br>
Mitigation: Keep the Confirm and Discard review step for pending calendar rows, and disable the skill in sensitive personal or workplace contexts where broad transcript monitoring is not appropriate. <br>
Risk: Event details can be wrong when transcript language is ambiguous or incomplete. <br>
Mitigation: Review pending event cards before confirming them, and correct ambiguous time, attendee, location, or note fields in the event's chat thread. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samuel-wei/skills/calendar-extractor) <br>
- [HiJavis iPhone app](https://apps.apple.com/us/app/hijavis/id6745134765) <br>
- [Route contract](artifact/references/route-contract.md) <br>
- [Prompt context fallback notes](artifact/docs/pr-drafts/2026-08-02-prompt-context-fallback.md) <br>


## Skill Output: <br>
**Output Type(s):** [json, markdown, shell commands, configuration] <br>
**Output Format:** [JSON event arrays, markdown event cards, and shell commands for fetch, push, anchor, and update flows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes pending event rows and per-event chat cards; event-level deduplication is kept in local per-user state for 30 days.] <br>

## Skill Version(s): <br>
0.7.2 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
