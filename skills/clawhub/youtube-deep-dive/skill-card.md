## Description:

Analyzes a YouTube video link to produce a timestamped transcript with speaker labels and key-frame notes, plus an in-depth summary of its main ideas, outline, key points, quotations, and mentioned entities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit YouTube links to obtain timestamped speech transcripts and key-frame descriptions, or request a structured summary for study and reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to share a secret API key in chat.

Mitigation: Do not request or paste secrets in chat; configure CUE_API_KEY locally through a secure mechanism, and revoke or rotate any key already shared.

Risk: Submitted video links are sent to Cue for processing and may consume paid credits.

Mitigation: Explain the service and credit implications before submission, and only send links the user is comfortable sharing with Cue.

## Reference(s):

- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-youtube-deep-dive)
- [Cue Omni Reader online experience](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown-formatted transcript and structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped speech and key-frame segments, speaker labels, and concise or detailed summaries. Visual descriptions are model-generated interpretations, and speaker labels do not establish real-world identities.]

## Skill Version(s):

1.0.0 (source: target release metadata; artifact frontmatter declares 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
