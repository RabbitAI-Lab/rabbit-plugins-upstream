## Description:

Transforms conversation transcripts and discussion notes into structured Notion-style documentation for knowledge capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to turn meeting transcripts, customer calls, architecture discussions, and interview notes into organized summaries, decision records, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local file and command capabilities for a documentation-formatting workflow.

Mitigation: Install and run it only in a scoped workspace, and grant file access or command execution only when the user explicitly intends those actions.

Risk: The skill claims sensitive information is automatically filtered, but the security evidence says that protection is overstated.

Mitigation: Redact confidential transcripts, customer details, credentials, and private meeting content before submission.

Risk: The skill may process API keys or external-service configuration during setup.

Mitigation: Use least-privilege credentials, keep secrets out of transcripts and version control, and rotate exposed keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-capture)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON structured documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution logs, capture metadata, and status fields.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter reports 0.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
