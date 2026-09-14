## Description:

Vaaya gives agents access to a paid API catalog for research, scraping, media generation, LLM routing, lead enrichment, live data, sandboxes, browser automation, email, storage, commerce, and tokenized-share workflows with quoted prices and per-call spending ceilings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marupelkar](https://clawhub.ai/user/marupelkar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to connect an agent to Vaaya's paid service catalog, route capability requests, run approved API calls, and configure MCP or API-key access with spending controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad authority to spend prepaid funds on external paid services.

Mitigation: Use strict per-call spending ceilings, account-level spending limits, and explicit user approval before paid actions.

Risk: The skill asks agents to retain credentials or tokens for future sessions.

Mitigation: Prefer OAuth or a dedicated secret manager, keep credentials out of shared repositories, chat messages, and logs, and revoke leaked keys promptly.

Risk: Installer flows may change agent MCP configuration and run unpinned packages.

Mitigation: Pin installer package versions where possible and review MCP configuration diffs before continued use.

Risk: Commerce, stock purchases, outbound messages, phone calls, automation, and real-person media generation can have high-impact effects.

Mitigation: Require explicit confirmation for the item, amount, recipient, content, and automation rule before taking those actions.

Risk: Screenshots, files, generated media, and persistent memory may contain sensitive data.

Mitigation: Store only what is needed for the task and avoid retaining sensitive screenshots or files unless the user has approved that retention.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/marupelkar/skills/vaaya)
- [Vaaya Homepage](https://vaaya.ai/?utm_source=clawhub&utm_medium=agent&utm_campaign=skill)
- [Vaaya API Catalog](https://vaaya.ai/api/catalog)
- [Vaaya Recipes](https://vaaya.ai/recipes)
- [Vaaya Agent-Readable Index](https://vaaya.ai/llms.txt)
- [Vaaya Full Tool Reference](https://vaaya.ai/llms-full.txt)
- [@vaaya/mcp Package](https://www.npmjs.com/package/@vaaya/mcp)
- [Setup - connecting Vaaya to your agent](references/setup.md)
- [Tools - the exact params of every Vaaya MCP tool](references/tools.md)
- [Research with Vaaya - OneSearch and research playbooks](references/research.md)
- [Data - picking the right paid data call](references/data.md)
- [Media generation - images, video, music, voice, demo videos](references/media.md)
- [GTM playbook - outbound with Vaaya](references/gtm.md)
- [Compute, browser, files, memory, LLM, phone calls](references/compute.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with JSON API-call examples, shell commands, configuration snippets, and links to generated or retrieved artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include paid-service plans, quoted per-call costs, async job identifiers, citations, file URLs, account setup guidance, and user-confirmation checkpoints.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
