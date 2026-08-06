## Description:

Product-audience-content alignment table generator that turns product information into a five-part e-commerce content alignment table centered on translating product claims into consumer-facing language and shootable visuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomeng](https://clawhub.ai/user/handsomeng)

### License/Terms of Use:

MIT-0

## Use Case:

External content e-commerce teams, product marketing managers, and content leads use this skill to align what a product is, who it is for, why buyers care, how to express selling points, and how competitor gaps should be handled. It produces a filled product-audience-content alignment table rather than an empty template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist onboarding state and reuse or append brand archive files, which may expose product strategy or brand deliverables in local storage.

Mitigation: Before use, decide whether to allow ~/.ljhskill/onboarding.json and current-directory ljh-档案 files, and avoid placing confidential product strategy in shared, backed-up, or multi-user directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomeng/skills/ljh-duiqi)
- [Publisher profile](https://clawhub.ai/user/handsomeng)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Files]

**Output Format:** [Markdown alignment table with structured sections and optional local archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and update onboarding state and brand archive files when the user permits local persistence.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
