## Description: <br>
Compress Pdf helps an agent compress a user-provided PDF by uploading it to Cross-Service-Solutions and polling until compression is complete. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and workflow operators use this skill to compress a user-provided PDF through a third-party compression service and return job status plus a download URL when complete. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDFs are uploaded to a third-party service, which can expose sensitive document contents. <br>
Mitigation: Use only for non-sensitive PDFs after explicit user consent and confirmation that the user accepts the third-party service's privacy and retention behavior. <br>
Risk: The artifact includes vague and unrelated marketing triggers, which can broaden when the skill is invoked. <br>
Mitigation: Tighten invocation guidance to PDF compression tasks and avoid using the skill for unrelated marketing or growth workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/compress-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [Markdown guidance with a structured JSON result] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The result may include job_id, status, download_url, file_name, and compression settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
