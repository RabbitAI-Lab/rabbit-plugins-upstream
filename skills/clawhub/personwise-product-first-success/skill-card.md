## Description:

Use when the user asks for Product First-Success Guide from supplied source materials to produce a grounded interactive digital-human course learners can interrupt with voice questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams and product educators use this skill to turn setup guides, manuals, help articles, and selected product materials into an interactive first-success course. The course is intended to shorten time to first value while keeping the learning content grounded in supplied evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or update a user-level PersonWise CLI binary.

Mitigation: Require explicit user approval before install or upgrade and use only the bundled, verified installer path described by the release.

Risk: The workflow uses browser OAuth and selected files or images may be uploaded to PersonWise.

Mitigation: Use browser-based authorization only, never handle credentials or secrets, and upload only user-named or explicitly selected sources.

Risk: Course creation can consume existing PersonWise course credits.

Mitigation: Treat a course creation request as authorization only for the requested number of courses and never purchase credits automatically.

Risk: Generated courses could imply unsupported real-world completion or safety validation.

Mitigation: Keep content evidence-locked, avoid certification or completion claims, and require qualified on-site confirmation for high-risk or regulated use.

Risk: Course access could be broader than intended.

Mitigation: Default the distribution target to private and change to link sharing, publication, or topic submission only when requested by the user.

## Reference(s):

- [Product First-Success Guide on ClawHub](https://clawhub.ai/personwiseai/skills/personwise-product-first-success)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown]

**Output Format:** [Markdown guidance with JSON-backed CLI workflow commands and links to the created course when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces an interactive digital-human quick-start course through PersonWise; course access defaults to private unless the user requests broader sharing.]

## Skill Version(s):

2.1.9 (source: server release metadata and skill attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
