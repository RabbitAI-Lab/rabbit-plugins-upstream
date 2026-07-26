## Description: <br>
Use when receiving code review feedback before implementing suggestions, especially when feedback is unclear or technically questionable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivansslo](https://clawhub.ai/user/ivansslo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to evaluate code review feedback before responding or implementing changes. It helps them clarify ambiguous requests, verify suggestions against the codebase, push back when needed, and apply fixes one item at a time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: If the agent is asked to reply in GitHub review threads, an unreviewed public or shared comment could be inaccurate or inappropriate. <br>
Mitigation: Review any externally posted comment before sending, especially on public or shared repositories. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/ivansslo/Supwrs/tree/main/skills/receiving-code-review) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, shell commands] <br>
**Output Format:** [Markdown guidance with inline command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces review-response guidance and implementation sequencing; does not require API keys or external services by default.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
