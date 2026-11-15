## Description:

YouTube search and transcript API for AI agents — free search and free caption transcripts, plus paid search at $0.005/call and paid transcript at $0.01/call in USDC on Base via x402. No account, no API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhgao](https://clawhub.ai/user/zhgao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search YouTube and retrieve available caption transcripts as structured text with timed segments for research, summarization, fact-checking, and locating statements in videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests incur USDC charges, and successful settlement has not been verified.

Mitigation: Use free routes when sufficient; before paid calls, authorize spending and verify the live payment amount and recipient.

## Reference(s):

- [ClawHub agent-transcript release](https://clawhub.ai/zhgao/skills/agent-transcript)
- [agent-transcript API](https://agent-transcript.fly.dev)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON search results or transcript text with timed segments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript availability depends on the video's captions; paid routes require USDC payment authorization.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
