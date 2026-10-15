## Description:

Helps draft an invention or utility-model patent from technical materials or an initial idea, with a separate checklist of facts to verify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, R&D teams, and patent practitioners use the skill to turn disclosures or early ideas into a patent first draft and review notes for professional revision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential or pre-filing invention materials are sent to the PatentMax service.

Mitigation: Get organizational approval and minimize or redact unnecessary sensitive details before submission.

Risk: An overridden service endpoint could receive invention disclosures or credentials.

Mitigation: Do not change PATENTMAX_BASE_URL unless the destination is fully trusted.

Risk: API credentials and locally cached trial data may be exposed if the user's environment is not protected.

Mitigation: Protect PATENTMAX_API_KEY and access to the ~/.patentmax cache.

Risk: Generated claims and inferred technical details may be mistaken for a filing-ready application.

Mitigation: Verify the separate review notes and have a patent professional finalize the draft before filing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-drafting)
- [Publisher profile](https://clawhub.ai/user/ip930)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Materials guide](references/materials-guide.md)
- [Workflow](references/workflow.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Text guidance and downloadable Word (.docx) files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separate patent draft and verification notes; claims require professional review before filing.]

## Skill Version(s):

1.1.3 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
