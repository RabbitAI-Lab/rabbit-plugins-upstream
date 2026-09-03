## Description:

Collect structured Google Shopping product records in bulk by keyword.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Google Shopping keyword collection jobs and retrieve structured product results by keyword.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chinese-language instructions may broaden activation to unrelated Instagram Reel requests.

Mitigation: Review and narrow Chinese trigger text before installing, especially in environments that use Chinese-language prompts.

Risk: The skill sends collection parameters to Dataify with DATAIFY_API_TOKEN and may consume account credits.

Mitigation: Confirm cost-affecting scope before external task submission, use stored token checks without exposing token values, and install only where this Dataify data flow is acceptable.

Risk: Immediate external task creation with weak confirmation can submit paid jobs for ambiguous requests.

Mitigation: Require confirmation for ambiguous, high-volume, multi-input, media-download, or otherwise credit-sensitive collection requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-google-shopping-keywords)
- [Dataify dashboard](https://dashboard.dataify.com?utm_source=skill)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder?platform=1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON collection results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Dataify collection tasks, wait for asynchronous completion, and summarize large JSON payloads while preserving access to raw results.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
