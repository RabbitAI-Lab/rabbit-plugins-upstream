## Description:

Structured Extraction helps agents turn unstructured text, webpages, and PDFs into machine-readable JSON using JSON mode, schema constraints, few-shot prompting, output priming, and a JSON repair helper.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to design reliable extraction prompts and post-process model output into valid JSON for document extraction, web field extraction, and data pipeline preprocessing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional learning workflow can persist free-form notes and preferences on disk.

Mitigation: Do not record sensitive document contents, personal data, credentials, or confidential workflow details in learning notes; periodically review or delete learned_patterns.json.

Risk: Malformed or over-repaired model output could produce incorrect structured data.

Mitigation: Validate repaired JSON against an explicit schema and fail clearly when required fields or types do not match.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/structured-extraction)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes helper scripts for JSON extraction, repair, validation, and optional local learning notes.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
