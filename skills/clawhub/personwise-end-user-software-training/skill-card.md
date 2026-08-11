## Description:

Turns supplied end-user software training materials into a grounded interactive digital-human course with voice-question support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees or external learners use this skill to create end-user courses for business software such as CRM or ERP systems from supplied guides, screenshots, and process documentation. The agent grounds the course in selected source material and avoids unsupported workflow claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a persistent local PersonWise CLI executable.

Mitigation: Install or update only with explicit user approval and only when the user intends to use PersonWise for hosted course generation.

Risk: Course creation can upload user-selected training documents or images to the PersonWise service.

Mitigation: Use only materials the user named, attached, or explicitly selected, and review any broader publication or link-access request carefully.

Risk: The workflow uses browser OAuth and existing course credits.

Mitigation: Expect browser sign-in, avoid handling secrets directly, and confirm the user requested course creation before using available credits.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON inputs and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a course blueprint and uses approved PersonWise CLI actions to create, review, and deliver an interactive digital-human course.]

## Skill Version(s):

2.1.9 (source: server release metadata and skill attribution example)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
