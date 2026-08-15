## Description:

我好牛AI智投 helps agents check brand visibility across major Chinese AI assistants, generate information-feed ad hooks, create 15-second spoken ad scripts, and report account credit balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dexun-inc](https://clawhub.ai/user/dexun-inc)

### License/Terms of Use:

MIT

## Use Case:

External users and marketing teams use this skill to ask an agent for brand AI visibility checks, ad hook ideas, short spoken-script drafts, and remaining API credit balance. The skill is intended for Chinese advertising and brand-positioning workflows that rely on the user's own Wohaoniu account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand names, categories, product briefs, and advertising needs are sent to the Wohaoniu service.

Mitigation: Install and use the skill only if you trust ai.wohaoniu.com with those inputs, and avoid submitting sensitive or confidential briefs unless that trust is established.

Risk: The Wohaoniu API key could be exposed if pasted into an agent conversation or echoed in output.

Mitigation: Configure WOHAONIU_API_KEY as an environment variable, do not paste the full key into chat, and rotate the key if it is disclosed.

Risk: Ad hook and script generation can consume credits from the user's Wohaoniu account.

Mitigation: Check account balance when needed and make users aware that generation requests may spend credits.

## Reference(s):

- [我好牛 API reference](references/api.md)
- [Source repository](https://github.com/DEXUN-inc/wohaoniu-zhitou-skill)
- [ClawHub listing](https://clawhub.ai/dexun-inc/skills/wohaoniu-zhitou-skill)
- [我好牛AI智投 service](https://ai.wohaoniu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese text and Markdown summaries with metrics, links, tables, compliance notes, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brand visibility checks may take 30-60 seconds. Hook and script generation can spend credits from the user's Wohaoniu account.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
