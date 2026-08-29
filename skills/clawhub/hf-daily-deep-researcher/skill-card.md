## Description:

Tracks Hugging Face Daily Papers and arXiv for configured research topics, then orchestrates specialist agents to produce light scans or deep research reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and technical teams use this skill to monitor recent AI papers, prioritize relevant work, and generate structured markdown reports for weekly scans or deeper literature reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile or memory data may be copied into persistent local research configuration during initialization.

Mitigation: Review the generated config.json and keywords.json before running scheduled scans, and remove any personal or sensitive research details that should not be retained.

Risk: Generated reports may be shared with a third-party cloud service if Feishu upload is configured.

Mitigation: Keep cloud upload disabled unless third-party sharing is intended, and verify the folder token and report contents before enabling upload.

Risk: Automatic or recurring scans can reuse stale configuration and save research history locally.

Mitigation: Review the configured research focus, output directories, and history settings before enabling periodic use.

## Reference(s):

- [Hugging Face Daily Papers GitHub mirror](https://raw.githubusercontent.com/AtharvaDomale/Daily-HuggingFace-AI-Papers/main/data/latest.json)
- [Hugging Face Daily Papers API](https://huggingface.co/api/daily_papers?date=YYYY-MM-DD)
- [arXiv API query endpoint](https://export.arxiv.org/api/query?search_query=all:KEYWORD&sortBy=submittedDate&sortOrder=descending&max_results=50)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Configuration, Guidance]

**Output Format:** [Markdown research reports with JSON configuration, tracking history, and intermediate analysis files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved locally by default; optional cloud upload is disabled unless configured by the user.]

## Skill Version(s):

5.2.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
