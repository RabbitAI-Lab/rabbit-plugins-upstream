## Description: <br>
Helps agents audit neat retrospective explanations in business cases, post-mortems, market commentary, and strategy lessons by checking selection bias, pre-event uncertainty, counterfactuals, and confidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to evaluate whether a clean story about a business, market, historical, or operational outcome is being mistaken for causal evidence. It guides the user toward base rates, counterfactuals, uncertainty, and cautious operational lessons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be over-applied, causing responses to be more skeptical of tidy explanations even when the user only wants a simple narrative summary. <br>
Mitigation: Use it when the user is drawing lessons from a retrospective story, post-mortem, market explanation, or strategy analogy; avoid it when the user explicitly wants narrative communication and already understands it is a compression. <br>
Risk: Applying the framework to domains with well-tested causal structures could add unnecessary uncertainty. <br>
Mitigation: Honor the skill's stated exclusions for physics, tested medical interventions, and other cases where the causal structure is genuinely well understood. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/narrative-fallacy) <br>
- [Narrative Fallacy source references](references/sources.md) <br>
- [Taleb's 9/11 Example + Business-History Critique](examples/talebs-911-example-business-history-critique.md) <br>
- [AI Changes Everything vs. Measured Enterprise ROI](examples/ai-changes-everything-vs-measured-roi-2023-2026.md) <br>
- [deciqAI Narrative Fallacy page](https://www.deciqai.com/c/narrative-fallacy) <br>
- [deciqAI machine-readable skill metadata](https://www.deciqai.com/s/narrative-fallacy.json) <br>
- [McKinsey State of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) <br>
- [U.S. BIS advanced-computing and semiconductor export controls](https://www.bis.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown Narrative-Fallacy Audit with structured analysis sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask stepwise coaching questions before producing a final audit; produces no code, shell commands, configuration, or files.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
