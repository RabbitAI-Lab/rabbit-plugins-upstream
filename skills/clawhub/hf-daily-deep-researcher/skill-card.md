## Description: <br>
HF Daily Deep Researcher coordinates multi-agent workflows that scan Hugging Face Daily Papers and arXiv, prioritize relevant papers, and generate periodic or deep-dive research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers and developers use this skill to monitor configured AI research areas, identify high-priority new papers, and produce weekly, monthly, or comprehensive Markdown research reports with analysis and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read USER.md, MEMORY.md, and recent memory files to infer research interests, then persist derived preferences locally. <br>
Mitigation: Review config.json before use, remove shipped profile values, and run it only in workspaces where those memory files may be used for paper-tracking personalization. <br>
Risk: The artifact includes Feishu cloud-report behavior and a configured folder token, while cloud behavior is under-disclosed in the release evidence. <br>
Mitigation: Remove or replace the folder token, keep cloud_upload disabled unless publication is intended, and require explicit approval before uploading reports. <br>
Risk: Unattended cron execution could repeatedly scan, store, and potentially publish research reports without fresh scope confirmation. <br>
Mitigation: Avoid unattended cron use until scan scope, storage location, and upload controls are reviewed and documented for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-deep-researcher) <br>
- [arXiv API](https://export.arxiv.org/api/query?search_query={query}&max_results=50) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown research reports with structured tables, paper analyses, trend summaries, validation notes, and occasional configuration or command guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save local report and history files; Feishu cloud publication should remain explicit and disabled unless intentionally configured.] <br>

## Skill Version(s): <br>
5.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
