## Description: <br>
Turns selected OpenClaw collaboration sessions into structured Markdown blog drafts for technical retrospectives, learning notes, or troubleshooting records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonleezy](https://clawhub.ai/user/jasonleezy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OpenClaw users use this skill to turn real agent collaboration history into Markdown drafts for technical posts, learning notes, and troubleshooting writeups. The skill is intended for sessions the user explicitly chooses and expects the user to review generated drafts before sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads selected local session history, which may contain secrets, credentials, customer data, or private paths. <br>
Mitigation: Run it only on sessions suitable for extraction and manually inspect the generated Markdown before publishing or sharing. <br>
Risk: Generated drafts may preserve inaccurate technical details or incomplete redaction from the source conversation. <br>
Mitigation: Review technical claims, code snippets, data, and redaction markers before using the draft publicly. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jasonleezy/skills/session2blog) <br>
- [Publisher Profile](https://clawhub.ai/user/jasonleezy) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown files plus terminal text with session summaries and writing instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes drafts to the configured local articles directory and supports platform style, language, template, session selection, and collaboration-trace options.] <br>

## Skill Version(s): <br>
1.1.10 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
