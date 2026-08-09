## Description: <br>
Merge multiple user-provided PDF files by uploading them to Cross-Service-Solutions, polling until completion, then returning a download URL for the merged PDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crossservicesolutions](https://clawhub.ai/user/crossservicesolutions) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to merge two or more PDF files through Cross-Service-Solutions and receive a structured result with the completed file's download URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDF files are sent to a third-party processing API. <br>
Mitigation: Use only documents you are comfortable sending to Cross-Service-Solutions, and review the provider's privacy, retention, and compliance terms before processing confidential, regulated, legal, financial, or proprietary PDFs. <br>
Risk: The skill requires a Bearer API key for the provider API. <br>
Mitigation: Provide the key through a secret or environment variable and do not echo, log, or include it in shared transcripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/crossservicesolutions/skills/merge-pdf) <br>
- [Cross-Service-Solutions API key registration](https://login.cross-service-solutions.com/register) <br>
- [Cross-Service-Solutions merge API base URL](https://api.xss-cross-service-solutions.com/solutions/solutions) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, API Calls, Files, Shell commands, Guidance] <br>
**Output Format:** [Structured JSON with job status, download URL, file name, and input file names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-selected PDF files and a user-provided Cross-Service-Solutions API key; sends selected PDFs to the provider for processing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
