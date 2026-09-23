## Description:

GPT-only reviewer workflow for Qwen Web using the authenticated ChatGPT Work/Codex Cloud Browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ciklopentan](https://clawhub.ai/user/ciklopentan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to obtain an independent Qwen Web review of important questions, engineering conclusions, or ambiguous analyses while preserving responsibility for final verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected prompts or excerpts are transmitted to Qwen Web and may be retained in the signed-in Qwen account like normal web chat history.

Mitigation: Use only material the user has authorized for Qwen review, avoid confidential or regulated data unless explicitly approved, and prefer short redacted excerpts when sufficient.

Risk: Qwen responses can be incorrect or overconfident if treated as authoritative.

Mitigation: Use Qwen as an advisory reviewer only; compare its output with primary sources and label unresolved claims, conflicts, and assumptions.

Risk: Browser login, CAPTCHA, 2FA, or session changes can block or alter the review workflow.

Mitigation: Verify the live Qwen session, model, and thinking mode before sending a task, and stop for manual handoff when authentication or security checks appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ciklopentan/skills/qwen-web-reviewer-gpt)
- [Publisher profile](https://clawhub.ai/user/ciklopentan)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown or plain-text synthesis with verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory review output; final conclusions remain the primary agent's responsibility.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
