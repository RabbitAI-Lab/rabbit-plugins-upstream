## Description:

Helps agent users and skill maintainers build, debug, harden, and verify AdMapix-style raw-data workflow helpers using practical local-first checklists, analysis, and implementation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, maintainers, and agent teams use this skill to turn AdMapix-style raw-data workflow demand into concrete plans, code guidance, setup hardening, reliability checks, and reusable implementation artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger terms and implicit invocation may cause the helper to activate for unrelated software or data tasks.

Mitigation: Narrow trigger terms or disable implicit invocation so it runs only for explicit AdMapix or raw-data workflow requests.

Risk: The skill produces guidance, code suggestions, shell commands, and configuration snippets that could be incorrect for a user's local environment.

Mitigation: Review generated steps before execution and run the included validation or test commands against the target project.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/software-data-admapix-raw-developer-helper)
- [Requirement plan](references/requirement-plan.md)
- [Popular ClawHub skill demand: ontology](https://clawhub.ai/skills/ontology)
- [Popular ClawHub skill demand: Agent Browser](https://clawhub.ai/skills/agent-browser-clawdbot)
- [Popular ClawHub skill demand: AdMapix](https://clawhub.ai/skills/admapix)
- [Hacker News demand signal](https://news.ycombinator.com/item?id=49320900)
- [SegmentFault JavaScript demand signal](https://segmentfault.com/t/javascript)
- [SegmentFault TypeScript demand signal](https://segmentfault.com/t/typescript)
- [SegmentFault raw data demand signal](https://segmentfault.com/q/1010000012550302)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include assumptions, validation notes, and remaining risks when relevant.]

## Skill Version(s):

0.20260818.40417 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
