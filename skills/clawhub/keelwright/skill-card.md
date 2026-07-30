## Description: <br>
Keelwright helps AI coding agents run autonomous or loop coding sessions with machine-enforced safety gates, autonomy controls, self-healing loop practices, and plain-language reporting for users who cannot review every line of generated code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ratingtesting](https://clawhub.ai/user/ratingtesting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, builders, and non-developer founders use Keelwright to add safety gates, loop controls, verification habits, and concise reporting to AI-generated coding workflows before autonomous runs, loop coding sessions, or commits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may cause an agent to write tracking files into a project and maintain cross-session memory. <br>
Mitigation: Review the bootstrap and memory behavior before use, and run in a workspace where generated tracking files are acceptable. <br>
Risk: The skill may direct local commands, unattended installs, QA tooling, network lookups, skill changes, or production rollback workflows. <br>
Mitigation: Use a sandbox or explicit approval policy for package installs, production actions, network access, and memory or skill modifications. <br>
Risk: Security evidence marks the release for review because opt-in boundaries are not clear for several autonomous behaviors. <br>
Mitigation: Review the QA prompt, self-patching guidance, cron guidance, and production rollback rules before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ratingtesting/skills/keelwright) <br>
- [Publisher profile](https://clawhub.ai/user/ratingtesting) <br>
- [Clawdis author profile](https://github.com/ratingtesting) <br>
- [README](README.md) <br>
- [Security gates](references/security-gates.md) <br>
- [Circuit breaker](references/circuit-breaker.md) <br>
- [QA testing](references/qa-testing.md) <br>
- [QA results](qa-results/README.md) <br>
- [Architecture map](assets/architecture.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code blocks, command examples, checklists, and project-file instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to write tracking files, run local checks, install QA tools, perform network lookups, and maintain cross-session memory when the host agent permits those actions.] <br>

## Skill Version(s): <br>
1.5.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
