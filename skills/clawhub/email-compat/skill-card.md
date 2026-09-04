## Description:

Helps agents write and verify HTML email rendering across email clients using caniemail.com data, layout guidance, and a JSON linter that reports unsupported, mitigated, and untested features with workarounds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, email designers, and agents use this skill to design, edit, or review HTML email templates and transactional messages for rendering compatibility across clients such as Outlook, Gmail, and Apple Mail. It is scoped to rendering compatibility, not sending, deliverability, authentication, list management, or ESP selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The linter reads HTML/CSS files or stdin supplied for review, so sensitive message content may be visible to the agent workflow.

Mitigation: Run it only on files intended for review, and avoid passing secrets, recipient data, or private production content in email examples.

Risk: The tool may contact caniemail.com and write a local dataset cache unless it is run offline.

Mitigation: Use --offline when network access is not desired, and use --refresh when a fresh caniemail.com dataset is required.

Risk: Email client support data can be untested or stale for some features and clients.

Mitigation: Treat untested verdicts and old last_test_date values as review flags, and perform client testing before relying on the result for production email.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shbernal/skills/email-compat)
- [Release changelog](https://github.com/shbernal/caniemail-ai-tooling/releases/tag/v0.2.1)
- [caniemail.com](https://www.caniemail.com)
- [caniemail.com data API](https://www.caniemail.com/api/data.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Code]

**Output Format:** [Markdown guidance with inline shell commands; CLI results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node 22+. The CLI can run offline from the bundled dataset or fetch and cache caniemail.com data; linting reads caller-provided HTML/CSS files or stdin.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
