## Description:

HyperFrames routes agent requests to create, edit, animate, render, inspect, validate, preview, publish, or batch-render HTML-based video and motion graphic projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and video production teams use this skill as the entry point for HyperFrames projects: it resumes project state, captures intent, chooses the appropriate workflow, and coordinates creation, editing, rendering, validation, and publishing of HTML-based video deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically run unpinned npm-based HyperFrames update or install commands that modify project dependencies and installed workflow skills.

Mitigation: Use it in projects where npm execution and workflow-skill updates are acceptable, and review package and skill changes after use.

Risk: The skill can drive website capture, media generation, rendering, and publishing workflows.

Mitigation: Run it only where those actions are authorized, and inspect generated assets, render outputs, and publication targets before release.

Risk: Routing decisions can send a request to an inappropriate video workflow when the subject, input, or intended deliverable is ambiguous.

Mitigation: Confirm the resulting BRIEF.md or ask the documented routing-only question when the owning workflow cannot be determined uniquely.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes)
- [The intent layer - one conversation, before any workflow runs](references/intent-interview.md)
- [Brief contract](references/brief-contract.md)
- [Brief format - BRIEF.md](references/brief-format.md)
- [Capability menu - what HyperFrames can bring to a video](references/capability-menu.md)
- [Production loop - from an approved plan to a delivered video](references/production-loop.md)
- [The review loop - plan, sketch, build](references/review-loop.md)
- [Storyboard format - STORYBOARD.md + parsed manifest](references/storyboard-format.md)
- [SCRIPT.md - locked narration](references/script-format.md)
- [Subagent dispatch - harness adapter](references/subagent-dispatch.md)
- [Skill installation and freshness](references/skill-lifecycle.md)
- [Frame worker - core contract](references/frame-worker-core.md)
- [Route: general-video](references/routes/general-video.md)
- [Route: product-launch-video](references/routes/product-launch-video.md)
- [Route: remotion-to-hyperframes](references/routes/remotion-to-hyperframes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and project files such as BRIEF.md, STORYBOARD.md, SCRIPT.md, HTML compositions, and frame-packet artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update project dependencies or installed HyperFrames workflow skills before render-affecting commands.]

## Skill Version(s):

1.0.33 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
