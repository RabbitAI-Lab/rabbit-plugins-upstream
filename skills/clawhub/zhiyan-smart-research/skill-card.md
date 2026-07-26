## Description: <br>
Zhiyan Smart Research searches Crossref and PubMed, then guides an agent to produce structured, citation-backed academic research reports with summaries, literature reviews, gaps, recommendations, and follow-up questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, students, and developers use this skill to turn academic questions into literature searches and structured research reports. It is suited for literature review, research gap analysis, citation-backed synthesis, research recommendations, and follow-up exploration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research queries are sent to Crossref and PubMed. <br>
Mitigation: Avoid confidential, unpublished, or sensitive research topics unless third-party literature lookup is acceptable. <br>
Risk: Generated research reports and topics may be saved locally under research/sessions for follow-up context. <br>
Mitigation: Review local retention expectations and delete saved session files when they are no longer needed. <br>
Risk: Citation-backed synthesis depends on retrieved paper metadata and the configured OpenClaw LLM. <br>
Mitigation: Review citations, DOI or PubMed links, and unsupported claims before using outputs in research or publication workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/zhiyan-smart-research) <br>
- [Publisher profile](https://clawhub.ai/user/caoling7878-arch) <br>
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills) <br>
- [Crossref Works API](https://api.crossref.org/works) <br>
- [PubMed E-utilities search API](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi) <br>
- [PubMed E-utilities summary API](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi) <br>
- [Report template](artifact/templates/report-template.md) <br>
- [Usage guide](artifact/USAGE.md) <br>
- [Security notes](artifact/SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown reports with citation markers, JSON paper search results, and skill-local Markdown session files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports follow a six-section structure and may be saved under research/sessions for follow-up context.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
