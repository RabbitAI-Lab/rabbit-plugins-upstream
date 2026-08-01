## Description: <br>
HF Daily Deep Researcher helps agents track Hugging Face Daily Papers and arXiv research, choose light-scan or deep-research workflows, and produce structured Markdown research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and research teams use this skill to monitor AI and machine-learning papers, analyze important work, and generate periodic or deep-dive reports tailored to configured research interests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External paper searches and fetched paper text can be incomplete, stale, or incorrectly parsed. <br>
Mitigation: Review arXiv IDs, citations, and key claims in generated reports before relying on them for research or business decisions. <br>
Risk: The skill saves reports, history, configuration, and intermediate analysis files locally. <br>
Mitigation: Run it in an appropriate workspace and clear report, history, and temporary files when they contain sensitive research context. <br>
Risk: Optional Feishu upload can move generated research reports into a cloud document system. <br>
Mitigation: Keep cloud upload disabled unless the workspace owner has intentionally authorized Feishu OAuth and document sharing. <br>
Risk: Subagent output can be truncated or delayed during paper reading, analysis, or report writing. <br>
Mitigation: Use the built-in completeness checks and quality-checker outputs, and manually inspect final reports when coverage matters. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-deep-researcher) <br>
- [Hugging Face Daily Papers](https://huggingface.co/papers) <br>
- [arXiv API](https://export.arxiv.org/api/query) <br>
- [arXiv Search](https://arxiv.org/search/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, configuration, guidance] <br>
**Output Format:** [Markdown reports, structured analysis summaries, quality-check findings, and local report/history files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are saved locally by default; Feishu upload is optional and disabled in the default configuration.] <br>

## Skill Version(s): <br>
5.2.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
