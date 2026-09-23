## Description:

Analyzes an academic paper supplied as a PDF attachment or URL and produces a dual-mode Markdown report with a researcher-focused deep analysis and a concise logic-and-value summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sterlingfrank1](https://clawhub.ai/user/sterlingfrank1)

### License/Terms of Use:


## Use Case:

Researchers, students, and analysts use this skill to turn a full academic paper into a structured, academically rigorous reading report and a shorter summary of the paper's core logic, findings, and value.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download and process arbitrary paper URLs, which can expose private or untrusted sources to the agent.

Mitigation: Use trusted academic domains or uploaded PDFs, avoid private or internal URLs and sensitive unpublished papers, and review URL handling before use.

Risk: Generated temporary analysis files and final reports may contain sensitive paper content.

Mitigation: Delete temporary and report files when they are no longer needed.

## Reference(s):

- [Part A report template](artifact/references/part-a-template.md)
- [Part B summary template](artifact/references/part-b-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Single Markdown report file with two sections separated by a horizontal rule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report includes Part A deep academic analysis and Part B concise core-logic summary.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
