## Description:

AWS SES helps agents guide sandbox-to-production setup, domain/DKIM/SPF verification, SMTP credential generation, and Sendy integration for Amazon SES.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airo7](https://clawhub.ai/user/airo7)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to configure, verify, and troubleshoot Amazon SES for application email, production access, SMTP credentials, bounce and complaint monitoring, and newsletter workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill helps operate AWS SES and includes utilities that can affect email sending and account configuration.

Mitigation: Use least-privilege AWS credentials, review proposed commands before execution, and prefer dry-run modes before setup or sending actions.

Risk: The SMTP password generator prints a usable derived SMTP password.

Mitigation: Run credential generation only in a private local terminal and avoid shared terminals, CI logs, transcripts, or other recorded sessions.

Risk: Incorrect email sending practices can harm sender reputation or compliance posture.

Mitigation: Verify current AWS SES requirements, maintain bounce and complaint handling, and confirm opt-in and unsubscribe practices before production sending.

## Reference(s):

- [ClawHub AWS SES Skill](https://clawhub.ai/airo7/skills/aws-ses-skill)
- [AWS SES production access documentation](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html)
- [AWS SES SMTP credentials documentation](https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html)
- [AWS SES DKIM documentation](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html)
- [Sendy Amazon SES integration](https://sendy.co/amazon-ses)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, Python snippets, and helper script outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper scripts may call AWS APIs through boto3 and may print generated SES SMTP credentials; dry-run options are available for setup and test-send workflows.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
