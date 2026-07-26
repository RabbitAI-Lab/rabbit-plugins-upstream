## Description: <br>
Grounded web search and research via Perplexity over SELAT, with default web search and optional agent-answer or deep-research escalations that require live price confirmation before paid use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[selat](https://clawhub.ai/user/selat) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to run grounded web searches, synthesize cited answers, and optionally escalate to paid Perplexity agent-answer or deep-research workflows when a normal search is not enough. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches and escalations can spend real USDC through SELAT. <br>
Mitigation: Run the free dry run first, show the live quote and spend limits, and get explicit user approval before wallet setup, funding, or any paid run. <br>
Risk: Agent-answer and deep-research escalations are separate paid calls from the default web search. <br>
Mitigation: Confirm the live price and user approval before every escalation, not only before the first search. <br>
Risk: Search results may be thin, stale, or insufficient for the user's question. <br>
Mitigation: Synthesize cited answers from returned source URLs, note the recency window, and clearly flag thin or stale results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/selat/skills/perplexity-search) <br>
- [SELAT Perplexity Search skill source](https://github.com/SELAT-AI/selat-skills/tree/main/skills/perplexity-search) <br>
- [SELAT skills documentation](https://github.com/SELAT-AI/selat-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and cited-answer synthesis instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid SELAT calls require a dry run, live quote review, and user confirmation before spending USDC.] <br>

## Skill Version(s): <br>
1.1.2 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
