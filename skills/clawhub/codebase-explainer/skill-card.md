## Description:

Produces a durable onboarding artifact for a codebase by creating or refreshing ONBOARDING.md with cited read-first notes, system overview, dependency map, startup flow, auth flow, and important files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate or refresh a durable repository onboarding document with cited codebase orientation, startup and auth flows, dependency usage, and key files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update ONBOARDING.md when ordinary codebase-orientation prompts are used.

Mitigation: Run it only in repositories where a documentation change is intended and review the generated diff before keeping it.

Risk: The onboarding document can expose repository structure, startup flow, auth flow, and important internal files.

Mitigation: Review the generated document for sensitive details before sharing or committing it.

Risk: The optional sharing step can upload the generated onboarding document.

Mitigation: Use sharing only after confirming the document is appropriate for the intended audience.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown file plus concise chat summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or refreshes ONBOARDING.md; substantive codebase claims are expected to cite file:line evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
