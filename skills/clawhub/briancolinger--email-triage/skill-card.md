## Description: <br>
IMAP email scanning and triage with AI classification via a local Ollama LLM that scans unread emails, categorizes them as urgent, needs-response, informational, or spam, and surfaces important messages for agent consumption with heuristic fallback when Ollama is unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[briancolinger](https://clawhub.ai/user/briancolinger) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to scan unread IMAP mailbox messages, classify their priority, and surface urgent or response-needed emails for agent workflows or periodic checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires IMAP credentials and processes private email metadata and message previews. <br>
Mitigation: Install only for mailboxes where this access is approved, prefer app-specific passwords, and limit credential exposure to the runtime environment that executes the skill. <br>
Risk: Email-derived content may be sent to the configured Ollama endpoint for classification. <br>
Mitigation: Keep OLLAMA_URL pointed at a local trusted Ollama server unless intentionally routing email-derived content elsewhere. <br>
Risk: The local JSON state file contains triage results and email previews that may be sensitive. <br>
Mitigation: Store EMAIL_TRIAGE_STATE in a protected path and treat the state file as sensitive mailbox-derived data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/briancolinger/skills/email-triage) <br>
- [Publisher profile](https://clawhub.ai/user/briancolinger) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text reports and optional JSON report output, with Markdown usage guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scans up to 20 unread emails per run, writes local JSON state, and reports unsurfaced urgent or needs-response emails.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
