## Description: <br>
Searches academic literature via arXiv, Semantic Scholar, and open-access PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and external users use this skill to find academic papers, build literature reviews, trace citation chains, and extract key details from open-access PDFs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger on broad PDF or paper-related requests. <br>
Mitigation: Confirm that the user wants academic paper search or PDF extraction before using the skill for ambiguous requests. <br>
Risk: Local PDF paths provided to the agent may expose file contents to document-conversion or reading tools. <br>
Mitigation: Only provide local PDF file paths that are intended for the agent to read. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-papers) <br>
- [Homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries with paper metadata, citation details, extraction notes, and source links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include guidance for converting open-access PDFs or local PDF files to markdown when a document-conversion tool is available.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
