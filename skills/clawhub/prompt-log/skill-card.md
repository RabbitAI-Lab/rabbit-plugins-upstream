## Description: <br>
Extract conversation transcripts from AI coding session logs (Clawdbot, Claude Code, Codex). Use when asked to export prompt history, session logs, or transcripts from .jsonl session files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesash](https://clawhub.ai/user/thesash) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use Prompt Log to export local AI coding session .jsonl logs into markdown transcripts for review, auditing, or sharing. It supports optional time filters and custom output paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exported AI session logs and transcripts can contain sensitive information. <br>
Mitigation: Treat source logs and generated transcripts as sensitive, avoid committing .prompt-log or transcript files to shared repositories, and choose a protected output path when needed. <br>
Risk: The skill runs a local extraction script against session history. <br>
Mitigation: Install only when local AI session history export is intended and inspect scripts/extract.sh before running it. <br>


## Reference(s): <br>
- [Prompt Log on ClawHub](https://clawhub.ai/thesash/skills/prompt-log) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown transcript file, with optional shell commands for extraction] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults output to .prompt-log/YYYY-MM-DD-HHMMSS.md; optional --after, --before, and --output parameters.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
