## Description: <br>
Merge Pdf uploads multiple user-provided PDF files to Cross-Service-Solutions, polls until the merge job completes, and returns job and download details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to merge multiple PDF files through an agent workflow and retrieve a structured result with merge status and a download URL. It is intended for routine document-processing workflows, not for encrypted-file cracking or tasks requiring complex human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user PDFs to Cross-Service-Solutions without enough data-handling detail. <br>
Mitigation: Use only PDFs that are appropriate for that external service until privacy, retention, and handling terms are verified; add an explicit confirmation step before upload. <br>
Risk: The security summary flags broad execution authority that is wider than a PDF merge workflow appears to need. <br>
Mitigation: Review before installing and narrow the skill permissions to PDF merging unless broader execution is specifically justified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/merge-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Guidance, Configuration] <br>
**Output Format:** [JSON result with job status and a merged PDF download URL when complete] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include job_id, status, download_url, file_name, and input_files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
