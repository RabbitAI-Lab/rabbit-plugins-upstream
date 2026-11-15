## Description:

Compare competitor and brand accounts across social platforms using recent posts, profile metrics, and engagement data from the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, competitive-intelligence, and brand teams use this skill to review public business or creator accounts, compare audience size and posting activity, and identify standout posts across supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a Weibo trends request outside the stated account-monitoring purpose.

Mitigation: Check that platform-wide Weibo trend data is needed for the task before using that request.

Risk: The skill requires an OKDATA_API_KEY, and scanner coverage was partial.

Mitigation: Verify the okdata API destination is trusted and necessary; keep the key in the environment and never expose it in prompts, logs, or output.

## Reference(s):

- [okdata API documentation](https://okdata.online/apis/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-competitors)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [Markdown tables with concise findings and linked sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-platform account comparisons, metric availability notes, and source and fetch details when available.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
