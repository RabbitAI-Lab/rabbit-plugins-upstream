## Description: <br>
Use when creating an interactive explainer about a codebase, repository, or source files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[analyticalmonk](https://clawhub.ai/user/analyticalmonk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create onboarding overviews, architecture maps, and deep dives for real codebases. It guides the agent to inspect source files, anchor claims to path-referenced snippets, and produce a self-contained interactive explainer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may read and summarize private code or secrets in the selected codebase. <br>
Mitigation: Use the skill only on repositories approved for summarization, and avoid pointing it at codebases containing secrets or private code that should not appear in an explainer. <br>
Risk: The generated explainer may include inaccurate claims or stale code snippets if the code changes or the agent relies on memory. <br>
Mitigation: Run the required fact-check gate against the actual implementation and verify every claim and quoted snippet against a specific path and line before delivery. <br>


## Reference(s): <br>
- [Explaining Codebases Skill Page](https://clawhub.ai/analyticalmonk/skills/explaining-codebases) <br>
- [Publisher Profile](https://clawhub.ai/user/analyticalmonk) <br>
- [Code Intake](references/code-intake.md) <br>
- [Code-Specific Figure Archetypes](references/code-figure-archetypes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Single self-contained interactive explainer with prose, path-referenced code snippets, and interactive figure code.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires fact-checking against the actual code paths and line references before delivery.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
