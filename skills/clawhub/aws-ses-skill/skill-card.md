## Description:

Amazon SES: sandbox -> production, domain/DKIM/SPF, SMTP credentials, and Sendy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airo7](https://clawhub.ai/user/airo7)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to configure Amazon SES for application or newsletter email, including sandbox status checks, domain/DKIM/SPF verification, production-access requests, SMTP credential generation, test sending, and Sendy integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AWS credentials, AWS account output, and derived SES SMTP passwords are sensitive.

Mitigation: Use least-privilege IAM permissions, run credential generation in a private local terminal, avoid sharing generated secrets or account status output, and rotate credentials if exposed.

Risk: Some helper scripts can call AWS SES APIs or send test email when dry-run mode is not used.

Mitigation: Run documented dry-run modes first, confirm the selected AWS region, domain, sender, and recipients, and execute only from an environment configured for the intended AWS account.

Risk: Support-case templates can misstate consent, bounce, complaint, or unsubscribe practices if placeholders are filled inaccurately.

Mitigation: Review and customize all template content so it matches the user's actual mailing practices, compliance obligations, and suppression handling before submission.

## Reference(s):

- [Server-resolved source repository](https://github.com/airo7/aws-ses-skill)
- [AWS SES production access documentation](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html)
- [AWS SES SMTP credentials documentation](https://docs.aws.amazon.com/ses/latest/dg/smtp-credentials.html)
- [AWS SES DKIM documentation](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim.html)
- [Sendy Amazon SES documentation](https://sendy.co/amazon-ses)
- [Support case reply template](templates/support-case-reply.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands, Python helper-script output, JSON status reports, and support-case templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sensitive AWS account status and SES SMTP credential output; dry-run modes are available for selected scripts.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
