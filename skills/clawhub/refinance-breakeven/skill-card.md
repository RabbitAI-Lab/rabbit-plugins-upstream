## Description: <br>
Compute the month a refinance actually starts saving money, including payment delta, breakeven month, total interest on both paths, and term-reset risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Borrowers, homeowners, and agents supporting financial analysis use this skill to compare an existing loan against a refinance offer, identify the breakeven month, and explain when lower payments may still increase total cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Refinance calculations may be incomplete or misleading if used directly for real financial decisions. <br>
Mitigation: Confirm the calculations independently or with a licensed professional before acting on the result. <br>
Risk: The skill references a helper script path that is not included in the package. <br>
Mitigation: Do not run an unrelated local file with the same path; use the skill's guidance only unless the intended helper script is supplied and reviewed. <br>


## Reference(s): <br>
- [Refinance Breakeven homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/refinance-breakeven.html) <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/refinance-breakeven) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with refinance calculations, verdict text, and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Educational financial model; asks users to verify results before real financial decisions.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
