## Description:

Helps users rewrite and design clearer application error messages that explain what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Application developers, support teams, SaaS operators, and users use this skill to turn vague errors into actionable messages, checklists, workflows, analysis, code changes, or support guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit triggers may route unrelated debugging or support requests into this workflow.

Mitigation: Explicitly invoke a different skill or state that this workflow should not be used when another troubleshooting process is intended.

Risk: Proposed wording for an error message can be misleading if the available failure context is incomplete.

Mitigation: Review assumptions, validate the revised message against the actual failure mode, and keep the final action clear for the affected user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Requirement Plan](references/requirement-plan.md)
- [MapLibre GL JS issue 8212](https://github.com/maplibre/maplibre-gl-js/issues/8212)
- [TestLink upgraded issue 433](https://github.com/sebiboga/testlink-upgraded/issues/433)
- [Poseidon HTTP Client issue 610](https://github.com/lodgvideon/poseidon-http-client/issues/610)
- [SegmentFault error-messages tag](https://segmentfault.com/t/error-messages)
- [Hacker News: I'm becoming AI-blind](https://news.ycombinator.com/item?id=49402160)
- [Hacker News: Sonic Pi v5](https://news.ycombinator.com/item?id=49248771)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown or plain text with optional code snippets, checklists, workflow steps, and validation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, remaining risks, and follow-up work when helpful]

## Skill Version(s):

0.20260824.40429 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
