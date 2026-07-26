## Description: <br>
Helps users find tech internships and new-grad jobs, track applications locally, and prepare interview or career-advice responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenyuan99](https://clawhub.ai/user/chenyuan99) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External job seekers, students, and career-support agents use Swelist to browse software engineering internship and new-grad listings, manage a local application tracker, and generate interview preparation or career guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Application tracking can create persistent local records that include job history, statuses, notes, and exported files. <br>
Mitigation: Confirm the SQLite database path and export destination before use, restrict file permissions where appropriate, and delete stale tracker data when it is no longer needed. <br>
Risk: Interview-prep prompts may include resume, background, or job data that is sent to OpenAI through jobgpt. <br>
Mitigation: Redact sensitive personal details before using jobgpt, avoid sending confidential employer or candidate information, and confirm OPENAI_API_KEY use is acceptable for the workflow. <br>
Risk: Live job listings and AI-generated career advice may be incomplete, stale, or inaccurate. <br>
Mitigation: Validate important job details against employer pages and review generated advice before using it in applications or interviews. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chenyuan99/skills/swelist) <br>
- [PyPI Project](https://pypi.org/project/swelist/) <br>
- [Source Repository Listed In Artifact](https://github.com/chenyuan99/swelist) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; tool output may be plain text, markdown, JSON, or CSV depending on the subcommand.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the swelist binary. The jobgpt workflow requires OPENAI_API_KEY. Tracker workflows may read and write a local SQLite database and export JSON or CSV.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata; artifact frontmatter lists 0.1.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
