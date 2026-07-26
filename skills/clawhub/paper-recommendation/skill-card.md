## Description: <br>
Automates discovery, parallel review, scoring, and briefing generation for AI research papers from arXiv. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sjf-ecnu](https://clawhub.ai/user/sjf-ecnu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and agent operators use this skill to find recent AI papers, generate parallel review tasks, extract paper content, and produce concise research briefings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The daily workflow can repeatedly send generated briefings to a fixed Telegram account. <br>
Mitigation: Remove or replace Telegram ID 8077045709 and confirm the intended recipient and message content before enabling the cron job or running daily_workflow.py. <br>
Risk: Private research topics, proprietary papers, or sensitive notes may be exposed through messaging delivery. <br>
Mitigation: Use local-only output for sensitive research material and avoid Telegram delivery unless the content and recipient have been reviewed. <br>
Risk: The documented cron command may use a path that does not match the installed skill location. <br>
Mitigation: Fix and verify the cron path before scheduling automated execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sjf-ecnu/skills/paper-recommendation) <br>
- [arXiv API](https://export.arxiv.org/api/query) <br>
- [arXiv abstract pages](https://arxiv.org/abs/) <br>
- [arXiv HTML papers](https://arxiv.org/html/) <br>
- [Poppler pdftotext](https://poppler.freedesktop.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefings, JSON paper and task records, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local PDF and briefing files under ~/jarvis-research/papers and can optionally send Telegram summaries when configured.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
