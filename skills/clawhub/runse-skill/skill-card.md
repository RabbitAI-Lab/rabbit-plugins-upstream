## Description:

A cloud text-polishing and formatting skill for Chinese long-form writing that calls a remote service to humanize or format novels, articles, and copywriting while aiming to preserve the original meaning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abcqq1234567](https://clawhub.ai/user/abcqq1234567)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to polish, format, or polish-and-format Chinese long-form text of at least 300 characters through a cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User text is sent to a remote cloud service for processing.

Mitigation: Use only with text suitable for remote processing and avoid confidential, regulated, or sensitive personal information.

Risk: Personal API keys can be saved locally in plaintext until cleared.

Mitigation: Do not paste personal API keys unless local plaintext storage is acceptable; clear saved keys when no longer needed.

Risk: The skill is marketed for reducing AI-detection signals, which may be inappropriate in academic, compliance, or platform-integrity contexts.

Mitigation: Use only where rewriting or formatting text is permitted and avoid use where policy requires original or machine-generated text handling.

Risk: Broad automatic triggering could process text the user did not intend to send to the cloud service.

Mitigation: Confirm intent before processing sensitive or ambiguous long-form text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abcqq1234567/skills/runse-skill)
- [Personal API key registration](https://apiuser-cesapi-ruanse-d7gq0uqzk1736f04d.webapps.tcloudbase.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON from the helper script, followed by polished or formatted text returned to the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires 300+ characters; modes include runse, paiban, and both.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
