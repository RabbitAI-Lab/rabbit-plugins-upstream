## Description:

Turns an invention idea or R&D materials into patent disclosure drafts and a companion review document, with optional invention-direction suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, engineers, and patent teams use this skill to turn technical materials into a draft disclosure and review notes for a patent professional, or to explore directions from an early idea.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential, unpublished, export-controlled, customer, or employer-owned invention material is sent to PatentMax for remote processing.

Mitigation: Submit only material you are authorized to share, after checking applicable confidentiality and data-handling requirements.

Risk: A custom service URL could send submitted invention material to a different server.

Mitigation: Check that PATENTMAX_BASE_URL is not overridden to an untrusted endpoint before submitting materials.

Risk: Generated disclosure details may include inferred facts, and patent comparisons do not establish patentability.

Mitigation: Review the companion notes and confirm technical facts with the inventor and patent professional before relying on the draft.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/invention-disclosure-writer)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Materials guide](references/materials-guide.md)
- [Disclosure workflow](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Files]

**Output Format:** [Conversational guidance and downloaded Word documents (.docx)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The disclosure and companion review notes identify inferred details and missing facts; idea exploration returns proposed directions and scores.]

## Skill Version(s):

1.1.3 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
