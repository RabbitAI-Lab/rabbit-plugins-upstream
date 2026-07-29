## Description: <br>
Grounded web search and research via Perplexity over SELAT, with keyless pay-per-call access, default web search, and optional user-approved research escalations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karensheng](https://clawhub.ai/user/karensheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need current, source-grounded web search results or a cited research brief. It is suited for queries about recent events, topic research, and deeper Perplexity-backed reports when the user approves the cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid searches spend USDC from the user's Circle Agent Wallet. <br>
Mitigation: Run the documented dry run first, show the live quoted price, and get explicit approval before wallet setup, funding, or any paid run. <br>
Risk: Agent answer and deep-research escalations are separate paid actions. <br>
Mitigation: Treat each escalation as a separate cost-confirmed action and proceed only after the user approves the live quote. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/karensheng/skills/perplexity-search) <br>
- [SELAT skill homepage](https://github.com/SELAT-AI/selat-skills/tree/main/skills/perplexity-search) <br>
- [SELAT skills documentation](https://github.com/SELAT-AI/selat-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and cited-answer expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid calls require a dry-run quote, user approval, and cost-aware synthesis with source URLs or citations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
