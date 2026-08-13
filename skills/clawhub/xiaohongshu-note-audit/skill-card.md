## Description:

Audits social content-marketing notes for policy compliance and shadowban or traffic-throttling risk, then returns risk flags and rewrite suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wsd-mj](https://clawhub.ai/user/wsd-mj)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to review social note copy before posting. It checks note text for banned words, absolute-claim wording, sensitive content, and shadowban or throttling risk, then suggests compliant revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted note content is sent to ai.wsdsocial.com for analysis.

Mitigation: Use the skill only when third-party transfer to that service is acceptable for the content being reviewed.

Risk: Users may include secrets, personal data, or confidential unpublished copy in the note text.

Mitigation: Remove sensitive data before audit unless policy and consent allow submitting it to the external service.

Risk: The skill requires WSD_API_KEY to call the audit service.

Mitigation: Store the API key in the environment and avoid pasting it into prompts, files, or shared command logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wsd-mj/skills/xiaohongshu-note-audit)
- [Server-resolved GitHub source](https://github.com/WSD-MJ/xhs-audit/tree/main/xiaohongshu-note-audit)
- [WSD Social skills portal](https://ai.wsdsocial.com/skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and API response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires WSD_API_KEY and sends submitted note content to ai.wsdsocial.com for audit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
