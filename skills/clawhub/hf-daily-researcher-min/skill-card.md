## Description: <br>
HF Daily Researcher Min helps agents search Hugging Face Daily Papers and arXiv, triage papers, read priority works, and produce lightweight or deep research reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomfoxxxx](https://clawhub.ai/user/tomfoxxxx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, developers, and research teams use this skill to monitor recent AI papers, conduct deeper literature reviews, and generate structured research reports from Hugging Face Daily Papers, arXiv, and related sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research interests and generated reports may contain sensitive or unpublished information. <br>
Mitigation: Run local-only for private research, avoid scheduled runs until configured, and review content before enabling any Feishu upload. <br>
Risk: Generated research summaries may be incomplete or need verification against source papers. <br>
Mitigation: Review generated reports and priority paper analyses before using them for decisions or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomfoxxxx/skills/hf-daily-researcher-min) <br>
- [arXiv API query endpoint](https://export.arxiv.org/api/query?search_query={query}&max_results=50) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown research reports with supporting local JSON or Markdown artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save reports locally and optionally create Feishu documents when configured.] <br>

## Skill Version(s): <br>
4.1.4 (source: server release metadata and artifact/config.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
