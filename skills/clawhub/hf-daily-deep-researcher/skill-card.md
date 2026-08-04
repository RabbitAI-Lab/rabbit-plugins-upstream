## Description: <br>
Dist orchestrates multi-agent workflows for Hugging Face Daily Papers and arXiv research tracking, supporting recent-paper scans and full-topic deep research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers and developers use this skill to track new AI papers, prioritize papers for deep reading, synthesize trends, and generate Markdown research reports for weekly scans or broad literature reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow saves research topics, intermediate analyses, reports, and scan history locally. <br>
Mitigation: Install only when local storage of this research material is acceptable, and review or clear local report and history directories according to the user's data handling needs. <br>
Risk: Generated reports can be uploaded to Feishu after authorization, which may expose report contents through that account or cloud document sharing. <br>
Mitigation: Keep cloud upload disabled unless the generated reports are suitable for the authorized Feishu account and its sharing settings. <br>
Risk: Research reports may contain incorrect paper metadata, experimental numbers, or claims if upstream sources or generated analyses are incomplete. <br>
Mitigation: Use the included quality-check workflow and verify key claims against original papers before citing or acting on the results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-deep-researcher) <br>
- [Hugging Face Papers](https://huggingface.co/papers) <br>
- [arXiv API](https://export.arxiv.org/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown research reports with structured tables, paper summaries, analysis sections, and optional local history files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local reports and scan history by default; optional Feishu upload is available only when authorized.] <br>

## Skill Version(s): <br>
5.2.1 (source: frontmatter, server release evidence, config.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
