## Description: <br>
Use when operating the 织信/Informat platform, including apps, tables, workflows, automations, scripts, APIs, dashboards, records, listeners, schedules, or platform-generated files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[informat365](https://clawhub.ai/user/informat365) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Informat administrators use this skill to query, configure, and operate Informat platform applications, data tables, workflows, automations, scripts, APIs, dashboards, records, listeners, schedules, and generated files. It is intended for sessions where the user needs guided platform operations with schema and documentation checks before mutating app or production data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can administer Informat teams and apps and mutate production data, including deletes and publishing. <br>
Mitigation: Install only for trusted users, use least-privilege Informat agent tokens, and require explicit human confirmation for destructive operations and publishing. <br>
Risk: The skill can create, save, and execute scripts or JavaScript-like operations that may affect data or system behavior. <br>
Mitigation: Review generated scripts before saving or running them, and require confirmation before using execution, system, process, or eval capabilities. <br>
Risk: The skill can send email, make web/API-oriented changes, and handle credential-adjacent Git or token configuration. <br>
Mitigation: Avoid granting the skill in shared or untrusted sessions, confirm outbound email and web calls, and protect any credentials with least-privilege and rotation practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/informat365/skills/informat) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Informat platform documentation index](artifact/references/doc/markdown/) <br>
- [Informat script API reference](artifact/references/doc/markdown/script/) <br>
- [call_informat.js](artifact/scripts/call_informat.js) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with command snippets, JSON parameter files, and generated platform code or configuration when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include downloadable file links returned by the Informat platform upload flow.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
