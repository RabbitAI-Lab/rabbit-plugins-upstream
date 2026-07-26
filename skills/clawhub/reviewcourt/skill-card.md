## Description: <br>
Reviewcourt helps agents turn completed Tencent Meeting requirement, PRD, or technical-design reviews into evidence-backed review recommendations with transcript citations, blockers, acceptance criteria drafts, and optional PRD comparison. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chris1wang3](https://clawhub.ai/user/chris1wang3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, developers, and review facilitators use this skill after a Tencent Meeting requirement, PRD, or technical-design review to determine whether the reviewed work should proceed, proceed with conditions, be rejected, or be marked information-insufficient. When a PRD or related document is provided, the skill also checks meeting conclusions against the document for omissions, conflicts, and newly added scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require Tencent Meeting CLI access to ended meeting records and transcripts. <br>
Mitigation: Confirm CLI installation and OAuth login yourself, and use the skill only for meetings you are authorized to review. <br>
Risk: OAuth credentials or internal meeting identifiers could be exposed if handled carelessly. <br>
Mitigation: Do not display access tokens or refresh tokens, do not include internal meeting_id values in reports, and keep authorization steps user-confirmed. <br>
Risk: A review verdict can be misleading when transcript access is missing, partial, or unsupported by direct quotes. <br>
Mitigation: Require paragraph-level transcript evidence for pass, conditional pass, or reject recommendations; otherwise return information insufficient with concrete follow-up evidence needs. <br>
Risk: Meeting transcripts and PRDs can contain sensitive business or personal information. <br>
Mitigation: Analyze only authorized materials, minimize irrelevant personal information in outputs, and avoid automatic external sharing or task creation. <br>


## Reference(s): <br>
- [Review Playbook](references/review-playbook.md) <br>
- [Reviewcourt Source Homepage](https://github.com/Chris1Wang3/HammerRoom-Skills/tree/master/reviewcourt) <br>
- [Reviewcourt Support](https://github.com/Chris1Wang3/HammerRoom-Skills/issues) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown review report with evidence tables, transcript citations, blocker lists, acceptance criteria drafts, and optional inline shell commands for Tencent Meeting CLI setup or access checks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are evidence-bound review recommendations, not official team decisions; the skill does not automatically modify PRDs, send messages, create tasks, or evaluate participant performance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact claw.json lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
