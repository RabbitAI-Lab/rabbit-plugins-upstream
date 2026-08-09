## Description: <br>
Cross-shift continuity and unresolved issue tracking system for restaurant and franchise operators. Captures wins, bottlenecks, and handoffs at end of shift, then actively tracks unresolved urgent items across shifts until they are confirmed closed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mcphersonai](https://clawhub.ai/user/mcphersonai) <br>

### License/Terms of Use: <br>
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) <br>


## Use Case: <br>
Restaurant operators and franchise managers use this skill to capture end-of-shift reflections, create urgent handoffs, and keep unresolved issues visible across shift changes until they are closed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operational records can include incidents, handoff notes, and other confidential store context. <br>
Mitigation: Confirm the companion memory engine is configured with the intended store boundaries and retention policy before installation. <br>
Risk: Operators may volunteer personal or customer-identifying details in free-text shift notes. <br>
Mitigation: Use roles instead of names where possible and omit the PII categories prohibited by the skill before writing records. <br>
Risk: Urgent items can remain visible across shifts and may consume operator attention if they are not closed or dropped deliberately. <br>
Mitigation: Review stale and repeatedly surfaced items, update owners and deadlines, and require a reason when an issue is dropped. <br>


## Reference(s): <br>
- [QSR Shift Reflection on ClawHub](https://clawhub.ai/mcphersonai/skills/qsr-shift-reflection) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown and plain-text operational records, prompts, summaries, issue boards, and weekly digests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces store-scoped reflection and open issue records; artifact describes no direct external delivery, file writes, database writes, API calls, or network transmission.] <br>

## Skill Version(s): <br>
2.0.2 (source: SKILL.md frontmatter, ClawHub release metadata, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
