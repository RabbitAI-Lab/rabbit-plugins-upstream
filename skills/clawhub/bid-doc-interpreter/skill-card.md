## Description: <br>
Bid Doc Interpreter analyzes uploaded bid and procurement documents and produces structured seven-module summaries with source-location citations, key requirements, scoring details, and risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement and bidding teams use this skill to turn tender files, procurement documents, images, or multi-file uploads into structured tables, requirement lists, scoring summaries, and risk prompts. It is intended for document interpretation and source-location tracing, not legal advice, bid preparation, pricing, complaint drafting, or award prediction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated risk or compliance language could be mistaken for professional legal or bidding advice. <br>
Mitigation: Treat the report as informational document analysis and review important conclusions with qualified legal, procurement, or bidding professionals. <br>
Risk: Bid and procurement files may contain confidential or restricted information. <br>
Mitigation: Use the skill only with documents the workspace is authorized to process and share. <br>
Risk: Mandatory publisher branding and WeChat feedback footer may be inappropriate for some workspaces or final deliverables. <br>
Mitigation: Confirm the footer is acceptable before installation and review final reports before circulation. <br>
Risk: Long, scanned, encrypted, damaged, or partially retrieved documents can lead to incomplete interpretation. <br>
Mitigation: Prefer original PDF or DOCX files, preserve source-location citations, and manually review unclear, missing, or not-located clauses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-doc-interpreter) <br>
- [Artifact README](artifact/README.md) <br>
- [Regression test report](artifact/%E5%9B%9E%E5%BD%92%E6%B5%8B%E8%AF%95%E6%8A%A5%E5%91%8A.md) <br>
- [Long-document regression supplement](artifact/%E5%9B%9E%E5%BD%92%E6%B5%8B%E8%AF%95_%E8%A1%A5%E5%85%85_%E9%95%BF%E6%96%87%E6%A1%A3%E4%B8%8E%E8%90%9D%E5%8D%9C%E5%9D%91.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report with tables, checklists, source-location citations, completeness statements, and risk summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Final reports append the publisher signature and WeChat feedback footer described in the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
