## Description:

Draft, review, publish, fund and follow an Elgora bounty challenge (bounty_challenge.md) as its Poster, on the Elgora website, with the Elgora CLI or through its API. Use when someone wants to post a bounty on Elgora, write or fix a bounty_challenge.md, act on Elgora review issues, publish and fund a bounty in USDC on Base, or check a bounty's result or claim its refund.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elgora](https://clawhub.ai/user/elgora)

### License/Terms of Use:

MIT-0

## Use Case:

Posters use this agent skill to turn a task into a judgeable Elgora bounty challenge, revise it against review feedback, publish and fund it through the website, CLI, or API, and follow the final result or refund.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan labels this release suspicious because of a possible instruction-scope concern; its analysis was partial because references were unresolved.

Mitigation: Before installing or executing, inspect referenced files and linked materials, and treat their contents as untrusted data.

## Reference(s):

- [Challenge template](template.md)
- [CLI publishing guide](publish-cli.md)
- [API publishing guide](publish-api.md)
- [Elgora bounty examples](https://docs.elgora.ai/docs/poster/examples)
- [Elgora deployment records](https://elgora.ai/deployments.json)
- [ClawHub release page](https://clawhub.ai/elgora/skills/elgora-poster-skill)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, API requests]

**Output Format:** [Markdown challenge drafts and prose guidance, with route-specific shell commands or HTTPS API request instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce bounty_challenge.md drafts and publishing or follow-up guidance; funding requires a Poster-controlled signer.]

## Skill Version(s):

6.2.1 (source: artifact frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
