## Description: <br>
Extracts high-frequency customer questions and best answers from desensitized customer-service conversation logs and produces a standard FAQ Markdown document, with optional Excel input conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenobiazizi](https://clawhub.ai/user/zenobiazizi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support, knowledge-base, and operations teams use this skill to mine desensitized service chat logs for recurring questions, standard answers, and a reviewable FAQ document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer-service logs may contain private customer data if used before desensitization. <br>
Mitigation: Use only logs that have already been stripped of customer private data before installing or running the skill. <br>
Risk: Generated FAQ entries may be incomplete or unsuitable for production knowledge bases without domain review. <br>
Mitigation: Have a business expert review the FAQ Markdown before importing it into a knowledge base. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Shell commands] <br>
**Output Format:** [Markdown FAQ file plus plain-text summary; optional shell command output when converting supported input files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [FAQ entries are sorted by question frequency; generated content should be reviewed before knowledge-base import.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
