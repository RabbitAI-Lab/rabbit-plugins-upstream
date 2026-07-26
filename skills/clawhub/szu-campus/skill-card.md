## Description: <br>
Guides agents to use the local szu-cli for Shenzhen University campus tasks, including login checks, notices, schedules, grades, GPA and ranking, degree plans, academic progress, campus credits, lectures, dorm electricity, sports reservations, library holdings, and CNKI/Wanfang metadata workflows while enforcing JSON output, privacy minimization, and dry-run/confirm rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[awesomehou](https://clawhub.ai/user/awesomehou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to map campus-service requests for Shenzhen University into safe szu-cli commands, parse JSON results, and summarize only the necessary private information. It is intended for local CLI-assisted campus queries and tightly confirmed state changes such as sports reservations or cancellations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Campus records can include grades, ranking, schedules, identity fields, reservations, and library or database activity. <br>
Mitigation: Minimize returned personal data, do not request passwords, cookies, tokens, browser profiles, traces, screenshots, or HAR files, and summarize only what is needed for the user's request. <br>
Risk: The skill depends on the external local szu-cli package to access Shenzhen University services. <br>
Mitigation: Review and trust the installed szu-cli separately, verify the local environment with doctor and auth status commands, and treat the installed CLI as the factual source. <br>
Risk: Sports reservations and cancellations can change campus system state. <br>
Mitigation: Use dry-run first, require a uniquely identified booking, slot, field, or order, and run confirmed actions only after the user explicitly asks for them. <br>
Risk: Academic database and attachment workflows can be misused for bulk downloads or access-control bypass. <br>
Mitigation: Limit downloads to user-specified single items through visible CLI-supported actions, avoid hidden links or batch downloads, and stop on access, rate-limit, or permission errors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/awesomehou/skills/szu-campus) <br>
- [README](README.md) <br>
- [Command routing](references/commands.md) <br>
- [Natural-language examples](references/examples.md) <br>
- [Error handling](references/errors.md) <br>
- [Privacy and safety](references/privacy-safety.md) <br>
- [Academic databases](references/academic-databases.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local szu-cli >= 0.2.0 and Node.js 20 or newer; state-changing sports actions require dry-run plus explicit user confirmation.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
