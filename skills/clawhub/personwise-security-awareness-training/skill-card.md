## Description:

Turns supplied security policies and awareness materials into an interactive digital-human course grounded in those sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Security, compliance, HR, or training teams use this skill to create a source-grounded employee security awareness course from their own policies, with learner questions and optional assessments handled through PersonWise.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or update a local PersonWise CLI.

Mitigation: Proceed only when the user intends to use PersonWise and approves the install or update; use the bundled bootstrap path and its checksum and target-path controls.

Risk: The workflow uses browser OAuth and may consume existing course credits.

Mitigation: Use browser OAuth only, do not handle passwords or tokens, create only the requested number of courses, and do not purchase credits automatically.

Risk: Selected source materials are uploaded to PersonWise for course creation.

Mitigation: Upload only user-selected materials or files separately approved after discovery, and avoid confidential policies unless PersonWise data handling is acceptable for the organization.

Risk: Generated awareness training could overstate outcomes or introduce unsupported security facts.

Mitigation: Ground the course in supplied materials, avoid certification or risk-elimination claims, and route suspected incidents to the reporting channels named in those materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-security-awareness-training)
- [PersonWise service descriptor](artifact/assets/service-descriptor.signed.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON blueprints and shell command invocations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a PersonWise interactive course or presentation through the CLI; final course URLs are reported only after fresh state proves the requested access mode is playable.]

## Skill Version(s):

2.1.9 (source: server release evidence and skill attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
