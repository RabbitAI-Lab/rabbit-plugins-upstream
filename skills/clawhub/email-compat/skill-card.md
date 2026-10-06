## Description:

Helps write and check HTML email for rendering compatibility across email clients using caniemail.com support data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and email designers use this skill to build and review HTML email templates, check client support for HTML and CSS features, and find rendering issues with suggested workarounds. It does not address delivery or sending mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refreshing compatibility data contacts caniemail.com and may cache data locally.

Mitigation: Use --offline to avoid network access and review local caching before use.

Risk: Email templates supplied to the linter are processed locally.

Mitigation: Only lint templates you are comfortable processing with this tool.

Risk: Bundled or cached compatibility data may be stale, and untested features have unknown support.

Mitigation: Check data-source and test-date warnings and test uncertain rendering in target email clients.

## Reference(s):

- [Email Compatibility on ClawHub](https://clawhub.ai/shbernal/skills/email-compat)
- [Can I Email compatibility data](https://www.caniemail.com)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown guidance and email markup; JSON compatibility reports from the bundled checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports client-specific support, untested features, and lint findings; does not send email.]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
