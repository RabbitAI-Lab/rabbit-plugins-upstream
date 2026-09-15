## Description:

Maintain one current 28-day running-and-strength direction from the latest available Garmin or Intervals.icu evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atomchung](https://clawhub.ai/user/atomchung)

### License/Terms of Use:

MIT-0

## Use Case:

External athletes and coaches use this skill to reassess a 28-day running-plus-strength direction, review planned versus actual training, decide what to do today, and preview calendar changes before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Important tool behavior and coaching guidance can come from a mutable remote MCP service before the skill reads training data or changes calendars.

Mitigation: Install only when the configured MCP service or athlete-operated gateway is trusted, and verify the connected host before use.

Risk: The skill may request access to training-provider data and calendar delivery capabilities.

Mitigation: Grant only authorization scopes the athlete is comfortable sharing, and require an exact preview plus explicit confirmation before any workout delivery or withdrawal.

Risk: Training recommendations could be mistaken for medical guidance.

Mitigation: Do not rely on this skill for medical diagnosis or medical advice.

## Reference(s):

- [Long Run Hybrid Coach skill page](https://clawhub.ai/atomchung/skills/long-run-hybrid-coach)
- [Pace and Stay Strong](https://paceandstaystrong.com/)
- [Pace and Stay Strong MCP endpoint](https://mcp.paceandstaystrong.com/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured training-plan summaries and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on connected Garmin or Intervals.icu evidence and an authorized MCP service before giving current training guidance.]

## Skill Version(s):

1.4.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
