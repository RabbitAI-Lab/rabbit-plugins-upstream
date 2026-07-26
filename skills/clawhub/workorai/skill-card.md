## Description: <br>
WorkorAI helps agents run candidate job-search and employer recruiting workflows through WorkorAI MCP tools, including ranked job matches, applications, job lifecycle management, candidate discovery, evidence-backed comparisons, invitations, and onboarding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[m14mgn-hash](https://clawhub.ai/user/m14mgn-hash) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External candidates use this skill to find WorkorAI-matched jobs, inspect fit, apply, manage saved jobs, and respond to invitations. Employers use it to manage jobs, search and compare candidates with evidence-backed explanations, invite candidates, and review applicants. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-activate on broad job-search or hiring requests while handling reusable WorkorAI account keys and sensitive marketplace data. <br>
Mitigation: Install and enable it only for intended WorkorAI candidate or recruiting workflows, treat WorkorAI MCP keys like passwords, and avoid pasting keys in untrusted sessions. <br>
Risk: Candidate and employer tools can perform consequential actions such as applying, accepting or declining invitations, changing job state, inviting candidates, or changing review status. <br>
Mitigation: Require an explicit same-turn confirmation for each state-changing action and do not batch or pre-authorize future actions. <br>
Risk: Saving a WorkorAI key can use an OS credential store and may fall back to a local shared file with 0600 permissions. <br>
Mitigation: Save keys only after explicit user consent, prefer OS secret storage when available, pass keys through stdin rather than command arguments, and disclose the storage path when a file fallback is used. <br>
Risk: Employer workflows can expose candidate profile, interview, match, applicant, and contact-related data within WorkorAI access controls. <br>
Mitigation: Use employer data only for the requested recruiting workflow, respect review-status contact gates, and disclose that evaluated WorkorAI candidates are discoverable by employers on the platform. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/m14mgn-hash/skills/workorai) <br>
- [Auth Flow](references/auth-flow.md) <br>
- [Candidate Catalog](references/candidate-catalog.md) <br>
- [Candidate Recipes](references/candidate-recipes.md) <br>
- [Candidate Troubleshooting](references/candidate-troubleshooting.md) <br>
- [Employer Catalog](references/employer-catalog.md) <br>
- [Employer Recipes](references/employer-recipes.md) <br>
- [Employer Troubleshooting](references/employer-troubleshooting.md) <br>
- [General Troubleshooting](references/troubleshooting.md) <br>
- [Candidate Login](https://workorai.com/candidate/login) <br>
- [Candidate MCP Access](https://workorai.com/candidate/home?tab=mcp) <br>
- [Employer Login](https://workorai.com/employer/login) <br>
- [Employer Dashboard](https://workorai.com/employer/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with MCP tool names, onboarding links, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include candidate and employer workflow recommendations, credential-handling steps, job and candidate summaries, evidence-backed comparisons, and confirmation prompts before state-changing actions.] <br>

## Skill Version(s): <br>
0.4.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
