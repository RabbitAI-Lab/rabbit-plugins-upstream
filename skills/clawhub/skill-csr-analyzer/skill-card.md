## Description: <br>
Analyzes user-provided PDF, Word, Excel, or text documents to determine whether clauses qualify as IATF 16949 Customer-Specific Requirements and produces confidence-scored, clause-by-clause findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, quality engineers, and auditors use this skill to classify uploaded automotive quality documents as IATF 16949 Customer-Specific Requirements and receive clause-by-clause, confidence-scored analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad document-review prompts when attachments are present, causing unrelated documents to be inspected. <br>
Mitigation: Use it for automotive quality or IATF 16949 CSR documents, and avoid uploading sensitive unrelated documents unless inspection is intended. <br>
Risk: Generated reports may contain analysis conclusions about the uploaded document in the working directory. <br>
Mitigation: Review report contents and handle the generated file according to the document's confidentiality requirements. <br>
Risk: The skill classifies CSR content but does not replace official customer confirmation, audit judgment, or compliance advice. <br>
Mitigation: Treat findings as decision support and have qualified reviewers confirm CSR classification before relying on it for audits or contractual decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-csr-analyzer) <br>
- [Server-resolved GitHub provenance](https://github.com/duding-engicool/skill-csr-analyzer) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown report with a concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates a CSR-report-<document>.md report file when analysis is performed; report content may include analysis conclusions about the uploaded document.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
