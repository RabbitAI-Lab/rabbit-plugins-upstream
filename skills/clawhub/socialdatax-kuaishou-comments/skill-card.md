## Description:

Helps agents retrieve and analyze Kuaishou/Kwai comments and replies through SocialDataX for audience feedback, sentiment themes, pain points, FAQs, and discussion summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to collect Kuaishou first-level comments and replies, then summarize themes, sentiment signals, objections, pain points, FAQs, and discussion patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls a third-party npm package and API service that require user trust before installation and use.

Mitigation: Confirm trust in the SocialDataX npm package and API service before installing or running commands.

Risk: API keys could be exposed if provided directly in prompts, command text, or generated files.

Mitigation: Provide the API key only through the SOCIALDATAX_API_KEY environment variable.

Risk: Unbounded pagination can increase cost or retrieve more data than intended.

Mitigation: Use --max-items instead of --all when limiting cost or data volume is important.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-comments)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Markdown, Guidance]

**Output Format:** [JSON data from SocialDataX plus Markdown summaries and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; supports pagination with page tokens and item limits.]

## Skill Version(s):

0.1.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
