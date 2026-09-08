## Description:

WPS Office 全家桶 helps agents automate Word, Excel, PowerPoint, document conversion, document templates, local office engine selection, optional AI-assisted office tasks, scheduled jobs, directory watching, usage statistics, and repair workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to create, edit, analyze, translate, summarize, convert, schedule, and manage office documents across WPS Office, Microsoft Office, LibreOffice, and pure Python fallback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad office automation can modify local documents and control local Office applications.

Mitigation: Back up important documents and review target file paths before allowing the agent to run write, export, conversion, or application-control commands.

Risk: Scheduled jobs and repair workflows can make persistent or high-impact system changes.

Mitigation: Require explicit user confirmation before registering scheduled tasks or running repair commands, and review any schtasks, crontab, or regsvr32 operation first.

Risk: External AI or speech services may receive document text, audio, meeting transcripts, prompts, or API-key-backed requests.

Mitigation: Prefer local-only modes for sensitive content and use remote model or speech processing only after explicit opt-in and credential handling review.

Risk: Local usage logs can retain operational metadata about document automation activity.

Mitigation: Keep logs local, avoid placing sensitive content in filenames or prompts, and rotate or delete logs according to the deployment policy.

## Reference(s):

- [ClawHub skill listing: WPS Office 全家桶](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [Publisher profile: fyniujin](https://clawhub.ai/user/fyniujin)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Architecture notes](artifact/ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and generated or modified office documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify local documents, control local office applications, register scheduled jobs, write local usage logs, and use external AI or speech services only when configured.]

## Skill Version(s):

5.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
