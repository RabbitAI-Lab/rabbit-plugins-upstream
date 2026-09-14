## Description:

Rewrites and formats Chinese AI-generated text into a more natural human style for novels, articles, copy, and other long-form drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abcqq1234567](https://clawhub.ai/user/abcqq1234567)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to polish, humanize, and format Chinese text of at least 300 characters while preserving the original meaning and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full drafts are sent to a fixed Tencent Cloud Function for processing.

Mitigation: Do not submit confidential, regulated, or sensitive text unless you trust the service operator and its retention claims.

Risk: Personal API keys may be saved locally in plaintext and sent with processing requests.

Mitigation: Use a narrowly scoped key, avoid saving it unless needed, and clear or rotate it if it was reused elsewhere.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abcqq1234567/skills/wenzi-runse)
- [Tencent Cloud Function processing endpoint](https://1257707270-955niawhww.ap-shanghai.tencentscf.com/bailian/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON from the helper script, with polished or formatted Chinese text in the result field and agent-facing guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports runse, paiban, and chained both modes; input text must be at least 300 characters.]

## Skill Version(s):

1.5.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
