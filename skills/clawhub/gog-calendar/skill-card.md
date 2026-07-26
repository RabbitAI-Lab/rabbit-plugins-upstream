## Description: <br>
Access and manage Google Calendar events with gogcli for cross-calendar agendas, keyword search, filtered outputs, and confirmation-gated calendar changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lstpsche](https://clawhub.ai/user/lstpsche) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to query Google Calendar across calendars, search events by keyword, filter noisy calendars such as holidays, and prepare calendar write actions that require explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar commands may run against an unintended Google Calendar account or modify events with incorrect details. <br>
Mitigation: Review which account gogcli is authenticated to and require explicit confirmation after summarizing create, update, delete, or RSVP details. <br>
Risk: Broad cross-calendar agenda and search queries may surface personal or noisy calendar entries that the user did not intend to include. <br>
Mitigation: Use the intended account, apply user-provided or conservative calendar exclusions, and mention material filtering in the response. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lstpsche/skills/gog-calendar) <br>
- [gogcli README](https://github.com/steipete/gogcli/blob/main/README.md?utm_source=chatgpt.com) <br>
- [gogcli AGENTS guidance](https://github.com/steipete/gogcli/blob/main/AGENTS.md?utm_source=chatgpt.com) <br>
- [Google Calendar Events list API](https://developers.google.com/workspace/calendar/api/v3/reference/events/list?utm_source=chatgpt.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text or JSON calendar summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses token-conscious plain output by default and JSON only when structure is needed for aggregation, deduplication, or write workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
