## Description:

Rewrites AI-generated Chinese text into a more natural human style and can format polished drafts for novels, blog posts, and copywriting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abcqq1234567](https://clawhub.ai/user/abcqq1234567)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to humanize and format Chinese long-form text when they provide at least 300 characters and explicitly request polishing, rewriting, AI-trace reduction, or formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted article text is sent to a fixed cloud polishing service.

Mitigation: Install only if this cloud processing is acceptable, and do not submit confidential drafts, personal data, passwords, or proprietary material.

Risk: Personal API keys may be stored locally and sent to the cloud service.

Mitigation: Use temporary keys when possible, avoid saving keys unless required, and rotate or revoke any personal key if exposure to the service endpoint is not acceptable.

Risk: The security verdict is suspicious because key handling and cloud transmission are not consistently disclosed.

Mitigation: Review the security summary and guidance before deployment, and restrict use to non-sensitive text unless the service and key handling model are approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abcqq1234567/skills/wenzi-runse)
- [Skill README](artifact/README.md)
- [Personal API key registration](https://apiuser-cesapi-ruanse-d7gq0uqzk1736f04d.webapps.tcloudbase.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON from the script, with polished or formatted Chinese text delivered to the user as plain text or Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least 300 characters of input text; the combined mode chains polishing followed by formatting.]

## Skill Version(s):

1.4.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
