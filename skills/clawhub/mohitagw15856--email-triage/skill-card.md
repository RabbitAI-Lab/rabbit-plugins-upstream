## Description: <br>
Triage a Gmail inbox down to only what needs you by surfacing recent emails that need replies, decisions, or follow-ups while filtering receipts, notifications, and newsletters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and other Gmail users use this skill to scan a recent inbox window, suppress low-value automated mail, and identify messages that need a reply, decision, follow-up, or awareness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Claude to read recent Gmail messages, which may include sensitive or personal information. <br>
Mitigation: Invoke it explicitly for a defined time window and use it only when you are comfortable granting access to those messages. <br>
Risk: Draft reply starters or priority classifications may be incomplete or incorrect. <br>
Mitigation: Review surfaced emails and any drafted replies before sending messages or making decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/email-triage) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/email-triage.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown triage report with priority sections, filtered counts, summaries, and reply starters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a configurable email time window, defaulting to the last 8 hours.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
