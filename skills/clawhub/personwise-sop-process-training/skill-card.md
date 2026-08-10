## Description:

Turns SOP documents and policy files into grounded interactive digital-human procedure courses that learners can interrupt with voice questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, trainers, and operations teams use this skill to convert user-supplied SOP, process, procedure, or policy materials into grounded interactive procedure training. It is intended for training from existing source materials, not for regulatory certification or drafting new SOPs from scratch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or update the user-local PersonWise CLI and requires browser OAuth.

Mitigation: Install or update only after explicit Host approval, use the bundled PersonWise bootstrap path, and keep OAuth in the browser without asking for passwords, tokens, OTPs, cookies, or callback secrets.

Risk: Selected SOP documents and policy files are uploaded to PersonWise for course creation.

Mitigation: Upload only files the user named, attached, or explicitly selected; disclose and request approval before uploading any file discovered by the Agent.

Risk: Course access settings and Topics submission can broaden visibility or consume existing course credits.

Mitigation: Create only the requested number of courses, never buy credits automatically, default unspecified distribution to private, and broaden access or submit to Topics only when the user explicitly asks.

Risk: Generated training could be mistaken for certification or operational authority.

Mitigation: Keep the course evidence-locked to supplied materials, name the source document and version, state that the document is authoritative when conflicts exist, and avoid claims that the course replaces supervision, licenses, statutory sign-off, or practical assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-sop-process-training)
- [PersonWise service](https://personwise.ai)
- [PersonWise CLI release origin](https://releases.personwise.ai/cli/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces course blueprints, PersonWise CLI commands, source-upload handling, review guidance, and concise status reports for interactive SOP course creation.]

## Skill Version(s):

2.1.9 (source: server release metadata and skill attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
