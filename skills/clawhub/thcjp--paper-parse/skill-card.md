## Description:

Analyzes a user-provided academic paper from a PDF attachment or URL and produces two reading reports: a deep researcher-focused analysis and a general-audience explanation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to turn a supplied academic paper into structured reading notes, including research questions, methods, findings, contributions, and two Markdown reports for different audiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file read/write access and command execution for paper and PDF processing.

Mitigation: Run it in a constrained workspace, review proposed commands and downloaded URLs before execution, and inspect generated files before sharing them.

Risk: Paper inputs may contain sensitive or unrelated documents.

Mitigation: Provide only the specific academic paper intended for analysis and avoid placing unrelated sensitive documents in the accessible workspace.

Risk: The security summary flags the release as suspicious because the artifact describes uses beyond academic-paper parsing.

Mitigation: Confirm the requested task stays within academic-paper analysis and reject unrelated automation, data-processing, or credential-handling behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/paper-parse)
- [Skill homepage from artifact metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports with concise summary text; examples also show JSON-shaped execution metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a researcher-focused analysis and a general-audience explanation for one supplied academic paper.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
