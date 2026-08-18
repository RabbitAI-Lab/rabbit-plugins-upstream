## Description:

PDF合并工具 helps agents upload multiple user-provided PDF files to Cross-Service-Solutions, poll the merge job until completion, and return job status plus a download URL when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to merge multiple PDF files through an agent workflow and receive structured status and download information for the merged result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User PDFs may be uploaded to an external service with unclear data-handling controls.

Mitigation: Confirm exactly which service receives the files and avoid confidential PDFs unless the service's privacy and retention practices are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/merge-pdf)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [Structured JSON object with merge job status and a download URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include job_id, status, download_url, file_name, and input_files.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
