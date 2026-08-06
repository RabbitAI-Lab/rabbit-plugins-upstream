## Description: <br>
Search a user-authorized Discord history archive through discrawl's bounded search and message commands. Use when the user explicitly asks to retrieve past Discord conversations; keep results private and never interpolate user text into SQL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to search a user-authorized local Discord history archive, retrieve bounded message results, and inspect channel or message context while keeping private archive data within the workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose private Discord message content, author identifiers, attachments, and raw payloads from a local archive. <br>
Mitigation: Search only the user-requested scope, keep results within the workspace, and require explicit approval before sending archive results to another channel or service. <br>
Risk: Advanced SQL access over private message data can be misused if user-supplied keywords, IDs, dates, or channel names are interpolated into SQL. <br>
Mitigation: Prefer bounded discrawl search/messages commands or the bundled helper script; use only operator-authored, fixed, read-only SQL when SQL is necessary. <br>
Risk: Overbroad searches can retrieve more private history than intended. <br>
Mitigation: Use channel, author, date, and limit filters where possible, and keep command limits bounded to the documented range. <br>


## Reference(s): <br>
- [Discrawl project homepage](https://github.com/openclaw/discrawl) <br>
- [Discrawl database schema reference](references/schema.md) <br>
- [ClawHub skill page](https://clawhub.ai/jonathanjing/skills/discrawl-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, SQL examples, and JSON-producing discrawl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce private Discord message excerpts or JSON search results when the agent runs bounded discrawl commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
