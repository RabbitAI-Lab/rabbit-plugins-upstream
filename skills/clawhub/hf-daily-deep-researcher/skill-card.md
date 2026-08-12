## Description:

HF Daily Deep Researcher helps agents track Hugging Face Daily Papers and arXiv, run light scans or deeper literature reviews, and produce structured research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developer agents use this skill to monitor new papers, prioritize relevant work, read selected papers in depth, synthesize trends, and write weekly, monthly, or deep research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The initializer can read local OpenClaw profile and memory files and persist inferred research interests.

Mitigation: Set research_focus manually in config.json, or run init.py only after confirming that reading local profile and memory files is acceptable.

Risk: Generated configuration and keyword files may contain inferred or stale research interests.

Mitigation: Review config.json and keywords.json before running searches or sharing generated reports.

Risk: Scheduled runs or Feishu upload could send reports to an unintended destination if enabled without review.

Mitigation: Keep cloud upload disabled or on-demand until the schedule, destination folder, and overwrite behavior have been confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-deep-researcher)
- [Publisher Profile](https://clawhub.ai/user/tomfoxxxx)
- [Hugging Face Daily Papers API](https://huggingface.co/api/daily_papers?date=YYYY-MM-DD)
- [arXiv API Query Endpoint](https://export.arxiv.org/api/query)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with supporting JSON configuration and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce local report files and optional upload guidance when configured by the user.]

## Skill Version(s):

5.2.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
