## Description: <br>
Parses academic papers and images into structured research cards covering the problem, methods, datasets, results, limitations, contributions, and critical assessment after SoMark document extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[soul-code](https://clawhub.ai/user/soul-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and engineers use this skill to turn papers or document images into parsed Markdown/JSON and a structured research card for literature review, research tracking, and team knowledge sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected papers or documents are sent to SoMark for parsing. <br>
Mitigation: Use this skill only for documents whose confidentiality, regulatory status, and proprietary content are acceptable under SoMark's terms and data handling. <br>
Risk: The SoMark base URL can be changed, which may send documents to an unexpected endpoint. <br>
Mitigation: Confirm the base URL is an official SoMark endpoint before running the parser. <br>
Risk: Each parse consumes the user's SoMark API quota. <br>
Mitigation: Confirm with the user before parsing and process papers sequentially for a shared SOMARK_API_KEY. <br>


## Reference(s): <br>
- [Paper Digest skill page](https://clawhub.ai/soul-code/skills/paper-digest) <br>
- [SoMark API endpoint for mainland China](https://somark.cn/api/v1) <br>
- [SoMark API endpoint outside mainland China](https://somark.ai/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Shell commands, Guidance, Analysis] <br>
**Output Format:** [Markdown research card plus parser-generated Markdown, JSON, and parse_summary.json files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOMARK_API_KEY; one SoMark API call is used for each parse; multiple papers are processed sequentially.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
