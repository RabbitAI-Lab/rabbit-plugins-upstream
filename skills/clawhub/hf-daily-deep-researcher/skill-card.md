## Description:

HuggingFace Daily Papers and arXiv multi-agent research system that runs light scanning or deep research workflows to find papers, analyze priority work, and produce research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and research teams use this skill to monitor HuggingFace Daily Papers and arXiv for new work in configured research areas, then produce weekly, monthly, or deep-dive Markdown research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read workspace profile, memory, and recent memory files during initialization.

Mitigation: Review init.py before running it and avoid initialization unless you consent to using local profile and memory context for configuration.

Risk: Configuration may include personal research focus, local history paths, and a Feishu folder token.

Mitigation: Review and clear config.json before use, keep cloud_upload disabled unless report publishing is intended, and rotate or remove any folder token not meant for the release environment.

Risk: Recurring runs and Feishu publishing can repeatedly generate and send research reports without enough up-front review.

Mitigation: Do not enable cron or cloud publishing until destination, retention, and review expectations are understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-deep-researcher)
- [Hugging Face Daily Papers API](https://huggingface.co/api/daily_papers?date=YYYY-MM-DD)
- [arXiv API query endpoint](https://export.arxiv.org/api/query?search_query=all:KEYWORD&sortBy=submittedDate&sortOrder=descending&max_results=50)
- [arXiv HTML paper view](https://arxiv.org/html/{arxiv_id})

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured research notes, JSON configuration updates, and occasional shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save reports locally and can upload to Feishu when explicitly configured.]

## Skill Version(s):

5.2.5 (source: server release metadata; artifact frontmatter reports 5.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
