## Description:

Worklittle Jobs MCP connects AI assistants to Worklittle for job search, applications, resume generation, cover letter generation, market insights, and employer ATS workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsonbuilds](https://clawhub.ai/user/johnsonbuilds)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers and employer users use this skill through an agent to search job listings, inspect job details, generate resumes and cover letters, submit Worklittle-hosted applications, and manage employer-side ATS records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using Worklittle can send resumes, cover letters, profile details, application materials, and employer ATS data to an external service.

Mitigation: Use scoped API keys and have the agent confirm the target job, data being sent, and any ATS record changes before submission.

Risk: Submitting applications through Worklittle can incur a small fee.

Mitigation: Require explicit confirmation of the target job and fee before applying, especially for repeated or bulk submissions.

Risk: Generated resumes and cover letters may need human review before they are sent to employers.

Mitigation: Review generated documents for accuracy, relevance, and appropriate disclosure before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsonbuilds/skills/worklittle-jobs-mcp)
- [Server-resolved GitHub import](https://github.com/johnsonbuilds/awesome-hermes-skills/tree/main/productivity/worklittle-jobs-mcp)
- [Worklittle Jobs MCP GitHub](https://github.com/worklittle/jobs-mcp)
- [Worklittle MCP documentation](https://docs.worklittle.com/mcp)
- [Worklittle Remote MCP](https://mcp.worklittle.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP tool-call guidance, JSON-style results, shell commands, and YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate resumes and cover letters in HTML, PDF, or DOCX through the Worklittle service.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
