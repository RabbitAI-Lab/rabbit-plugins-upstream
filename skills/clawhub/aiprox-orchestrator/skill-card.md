## Description:

Run a multi-step task on AIProx (aiprox.dev), paid in Bitcoin Lightning sats. Use it when the user asks to run a task through the AIProx orchestrator or to buy one of its capabilities. Orchestrate is 50 sats: one task, up to 4 steps on AIProx's own bots, one summarized answer. Single capabilities have their own prices: AI web answer 35, page text extract 20, summarize 40, translate 40. Payment is a LightningProx spend token or L402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[unixlamadev-spec](https://clawhub.ai/user/unixlamadev-spec)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when a user requests AIProx's paid orchestration or individual capabilities such as web answers, page extraction, summarization, or translation. It returns the requested result as text after the user approves the applicable cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Calls incur Lightning charges, and task text and supplied URLs or content are sent to AIProx for processing.

Mitigation: Confirm the endpoint price before each paid call and keep secrets and personal information out of tasks.

Risk: The optional spend token is a bearer credential; callback destinations receive task output, and requested messaging can send content externally.

Mitigation: Use a minimally funded token, never expose it in tasks or logs, use only HTTPS callback endpoints you control, and confirm the recipient and message content before sending.

## Reference(s):

- [AIProx](https://aiprox.dev)
- [AIProx Documentation](https://aiprox.dev/docs.html)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Text response containing a summary, extracted page text, translation, or other requested capability result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Web answers may include up to five source links; available result types depend on the requested capability.]

## Skill Version(s):

3.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
