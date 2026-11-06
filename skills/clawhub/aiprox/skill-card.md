## Description:

Pay-per-call tasks on AIProx (aiprox.dev), paid in Bitcoin Lightning sats. Use it when the user asks to run a task through AIProx or to buy one of its capabilities. Orchestrate is 50 sats: one task, up to 4 steps on AIProx's own bots, one summarized answer. Single capabilities have their own prices: AI web answer 35, page text extract 20, summarize 40, translate 40. Payment is a LightningProx spend token or L402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yebdmo2](https://clawhub.ai/user/yebdmo2)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when a user requests AIProx's paid search, page extraction, summarization, translation, or orchestration services. Calls send task inputs to AIProx and require user approval for the stated price before spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests send task inputs to AIProx and may incur a Lightning charge.

Mitigation: Confirm the endpoint and price with the user before each paid call; use a minimally funded spend token and do not retry without approval.

Risk: Tasks may contain sensitive information, and the spend token is a bearer credential.

Mitigation: Keep secrets and personal data out of task inputs; never print or log the token and fund it only for the intended spend.

Risk: A callback URL receives task results by POST.

Mitigation: Use only an HTTPS callback endpoint controlled by the user, and confirm outbound message recipients and content before sending.

Risk: Search content has restrictions on storage, redistribution, resale, and model training.

Mitigation: Use search responses only for the user's own use and follow the linked service terms.

## Reference(s):

- [AIProx documentation](https://aiprox.dev/docs.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Summaries, Translations, Source links]

**Output Format:** [AIProx API responses containing text or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The returned content depends on the selected capability; orchestration returns one summarized answer.]

## Skill Version(s):

4.0.0 (source: frontmatter, changelog, released 2026-11-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
