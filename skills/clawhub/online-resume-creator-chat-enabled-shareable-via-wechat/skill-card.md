## Description:

Generates a single-file HTML resume with a keyword-matched conversational assistant and WeChat sharing assets, including a cover image and QR-code share card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[peterzhangzihui](https://clawhub.ai/user/peterzhangzihui)

### License/Terms of Use:

MIT

## Use Case:

Developers, resume authors, and job seekers use this skill to turn structured resume information into a shareable personal resume page with a simple question-answer interface and WeChat-friendly sharing images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Published resume pages may expose personal contact details, salary expectations, or other sensitive resume information through a public link.

Mitigation: Review and remove sensitive fields before publishing; use a password gate or backend access control for sensitive resumes.

Risk: The built-in expiration check is a front-end notice rather than real access control.

Mitigation: Use backend authorization or password protection when access must actually expire or be restricted.

Risk: The resume assistant uses keyword matching and may not answer questions outside predefined resume sections.

Mitigation: Review the keyword rules and section text before sharing; use a backend LLM integration only when free-form answers are required.

## Reference(s):

- [Quickstart](references/quickstart.md)
- [WeChat Sharing and Distribution Reference](references/wechat-sharing.md)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Python command examples; generated files include a static HTML resume and PNG sharing assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated resume is static and offline; cover and QR-code card generation require Pillow and qrcode.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence, artifact _meta.json, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
