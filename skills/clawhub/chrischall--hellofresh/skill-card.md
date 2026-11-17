## Description:

Helps users review and plan their HelloFresh US meal-kit subscription, including delivery weeks, menus, meal picks, and confirmation-gated plan changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HelloFresh US subscribers use the skill to check delivery details, review menus and recipes, plan meals, and request subscription changes after confirming each proposed change.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Changes can affect upcoming deliveries or the subscription schedule.

Mitigation: Review the proposed change, confirm it explicitly, and check the reported verification status afterward.

Risk: The skill relies on a signed-in HelloFresh browser session and an unofficial web-app interface that may change.

Mitigation: Use the browser already signed in to HelloFresh; if session access or the interface fails, resolve that issue before retrying the requested action.

## Reference(s):

- [HelloFresh US](https://www.hellofresh.com)
- [HelloFresh MCP package](https://www.npmjs.com/package/@chrischall/hellofresh-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Natural-language summaries, recommendations, and instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Subscription changes require explicit confirmation and are reported with a verification status.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
