## Description:

Generates competitor patent analysis reports from PatSnap professional patent search queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, competitive intelligence teams, and developers use this skill to run PatSnap search expressions and produce competitor patent and literature reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be persisted in local .env files or loaded from a shared fallback location.

Mitigation: Use scoped PatSnap credentials, prefer platform secret storage where available, avoid production keys, and review or remove shared .env fallback paths before use.

Risk: The skill makes automatic network calls to PatSnap patent and literature APIs and may call ARK when configured.

Mitigation: Run it only in environments where those external calls are approved, and review query content for confidential information before execution.

Risk: Generated reports, HTML files, and patent images are persisted locally.

Mitigation: Inspect and clean the reports directory before sharing outputs or packaging the skill.

Risk: The run script can install Python dependencies automatically.

Mitigation: Review dependency installation behavior and execute the skill in a controlled Python environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/competitor-skill)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown reports with optional HTML files and local images; chat output may include selected report sections and configuration prompts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a PatSnap API key; optional literature and ARK keys enable literature retrieval and AI summarization.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
