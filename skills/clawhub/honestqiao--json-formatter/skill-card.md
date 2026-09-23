## Description:

Format, validate, compress JSON data, and extract JSON paths for improved readability and structure verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[honestqiao](https://clawhub.ai/user/honestqiao)

### License/Terms of Use:


## Use Case:

Developers and general users use this skill to reformat, validate, compress, and inspect paths in user-supplied JSON data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chinese-language instructions may be harder to review for English-only operators.

Mitigation: Review the artifact instructions before installation and confirm the behavior matches local policy.

Risk: Malformed or unexpectedly large JSON input can return parse errors or consume unnecessary agent context.

Mitigation: Use bounded, user-supplied JSON snippets and inspect validity or error fields before using results downstream.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/honestqiao/skills/json-formatter)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON object containing formatted JSON text, validity status, size, paths, or error details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operates on user-provided JSON strings; indentation defaults to two spaces when not specified.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
