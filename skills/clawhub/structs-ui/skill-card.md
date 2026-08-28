## Description:

Structs UI helps developers build Structs dashboards, forms, menus, HUDs, companion apps, and clients using SUI and the linked Structs client references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build Structs-themed interfaces and clients, including dashboards, forms, HUDs, transaction-signing flows, proof-of-work clients, GRASS listeners, and Desktop extensions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downstream Structs clients may handle wallet signing, permissions, or user confirmation incorrectly.

Mitigation: Review the linked Structs docs and require explicit transaction signing, permissions, and user confirmation before deployment.

Risk: SUI assets can fail silently when served from a subpath because their URLs are root-absolute.

Mitigation: Serve SUI assets from the root path or rewrite root-absolute URLs, then verify icons and form art in a browser.

Risk: Reference-client transaction failures may be silent if the downstream app does not surface settled events.

Mitigation: Add operator-visible error handling for transaction settlement and failure states in any generated client workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-ui)
- [Structs repository guidance](https://structs.ai/develop/repos)
- [Structs UI documentation](https://structs.ai/develop/ui/)
- [Structs UI tokens](https://structs.ai/develop/ui/tokens)
- [Structs UI components](https://structs.ai/develop/ui/components)
- [Structs UI runtime](https://structs.ai/develop/ui/runtime)
- [Structs UI gotchas](https://structs.ai/develop/ui/gotchas)
- [Structs UI patterns](https://structs.ai/develop/ui/patterns)
- [Structs UI examples](https://structs.ai/develop/ui/examples/README)
- [Structs client documentation](https://structs.ai/develop/client/)
- [Structs client actions and signing](https://structs.ai/develop/client/actions-and-signing)
- [Structs client proof-of-work](https://structs.ai/develop/client/work-and-pow)
- [Structs GRASS realtime events](https://structs.ai/develop/client/realtime-grass)
- [Structs Desktop extensions](https://structs.ai/develop/client/desktop-extensions)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes agents to Structs SUI and client references; no executable install behavior.]

## Skill Version(s):

1.25.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
