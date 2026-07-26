## Description: <br>
Analyze tender and procurement documents (PDF, Word, images) to extract qualification requirements, scoring criteria, key deadlines, prohibited clauses, and submission checklists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[soul-code](https://clawhub.ai/user/soul-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, bid, and proposal teams use this skill to parse tender, RFP, RFQ, and procurement documents, then produce a structured analysis of requirements, scoring criteria, deadlines, disqualifiers, contacts, and submission checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and RFP content is uploaded to SoMark for parsing. <br>
Mitigation: Use the skill only when policy permits sending the document contents to SoMark, and review procurement-data rules before processing confidential files. <br>
Risk: The skill requires SOMARK_API_KEY. <br>
Mitigation: Set the key through the environment and keep it out of chat, shared logs, screenshots, and committed files. <br>
Risk: AI-assisted tender extraction can miss, misread, or overstate procurement requirements. <br>
Mitigation: Verify extracted requirements, deadlines, disqualifiers, and recommendations against the original tender before submitting a bid. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/soul-code/tender-analyzer) <br>
- [SoMark API endpoint](https://somark.tech/api/v1) <br>
- [SoMark API Workbench](https://somark.tech/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tender analysis report plus local Markdown, JSON, and parse summary files from the parser script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local tender file path and SOMARK_API_KEY; parser output can be configured with output, element, and feature-format options.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
