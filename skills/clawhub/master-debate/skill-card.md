## Description:

Use when a user explicitly asks for an adversarial, multi-round dialectic between Buddhist masters, selecting or resolving two masters and orchestrating fresh subagent rounds with neutral closing observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xr843](https://clawhub.ai/user/xr843)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run structured, source-cited debates between Buddhist master personas when a prompt asks for adversarial comparison rather than a single-round overview. The skill guides master selection, round limits, subagent isolation, citation constraints, and a non-judgmental final summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on related prebuilt master metadata and reference files to resolve names, citations, and cross-critique material.

Mitigation: Install and review the expected prebuilt master files before use, and treat missing cross-critique coverage as a degraded debate rather than a blocker.

Risk: Multi-round fresh subagent orchestration can increase latency and token cost.

Mitigation: Use the configured round bounds, including the default 4 rounds and maximum 6 rounds, unless a narrower limit is appropriate.

Risk: Generated debate text can mislead readers if citations or doctrinal claims are unsupported.

Mitigation: Require each cited source identifier to exist in the relevant master source metadata and preserve the skill's neutral, no-verdict final summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xr843/skills/master-debate)
- [Publisher profile](https://clawhub.ai/user/xr843)

## Skill Output:

**Output Type(s):** [markdown, guidance]

**Output Format:** [Markdown debate transcript with cited rounds and a neutral summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default debate length is 4 rounds with a configured maximum of 6 rounds.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter/meta.json report 0.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
