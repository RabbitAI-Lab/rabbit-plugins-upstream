## Description:

This skill helps users draft Chinese official documents across common document types with structure guidance, style conventions, missing-information placeholders, and optional Word-format guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yourtsao](https://clawhub.ai/user/yourtsao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and office document-writing staff use this skill to draft, structure, and refine Chinese-language official documents such as requests, reports, summaries, notices, meeting minutes, speeches, and briefings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document-writing prompts are sent to the external service at gongwen-api.xyz.

Mitigation: Avoid submitting confidential personnel, legal, financial, internal government, or sensitive business material unless the provider's privacy and retention terms are acceptable.

Risk: A user account token may be stored locally in config.json after registration.

Mitigation: Protect the local configuration file, do not publish it, and rotate or re-register if the token is exposed.

Risk: The skill includes paid API use and email registration.

Mitigation: Confirm the user understands the registration, quota, and payment flow before using paid functionality.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yourtsao/skills/offical-paper-wrighting-chinese-skill)
- [README.md](artifact/README.md)
- [说明.md](artifact/说明.md)
- [Word export guidance](artifact/references/word-export.md)
- [Disclosed service domain](https://gongwen-api.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Chinese prose or Markdown, with optional Python code for Word document generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include missing-information placeholders such as 〔待补〕 when required facts are not supplied.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
