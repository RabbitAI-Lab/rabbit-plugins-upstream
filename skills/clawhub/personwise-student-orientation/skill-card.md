## Description:

Turns supplied student orientation materials into a grounded interactive digital-human course that learners can interrupt with voice questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External education and student-services teams use this skill to turn institution-provided orientation handbooks, policy documents, and imagery into an interactive course for incoming students.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update a local PersonWise CLI.

Mitigation: Require explicit user approval and use only the bundled official bootstrap and release sources before installation or upgrade.

Risk: The workflow uses browser OAuth and can upload course materials to PersonWise.

Mitigation: Use browser OAuth without handling secrets, upload only user-selected or explicitly approved files, and report only secret-free status.

Risk: The skill can create courses using existing credits and change access or publish when requested.

Mitigation: Treat course creation as bounded credit authorization, never purchase credits automatically, default access to private, and broaden sharing only on request.

Risk: Student orientation content may include consequential policies such as fees, visas, housing, accessibility, or safety.

Mitigation: Ground claims in supplied materials, route individual or consequential cases to named offices, and identify the source document and year used.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Text]

**Output Format:** [Markdown guidance with JSON inputs, shell command invocations, and concise status reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces PersonWise course workflow instructions and may return run IDs, project IDs, source statuses, and access URLs.]

## Skill Version(s):

2.1.9 (source: server release evidence and skill attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
