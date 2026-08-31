## Description:

Scrape Creators (scrapecreators.com). Use this skill for Scrape Creators requests involving searching and reading data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Scrape Creators discovery, credit-balance, and documented endpoint requests through an OOMOL-connected account instead of calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can spend Scrape Creators API credits when invoking documented endpoints through the connected account.

Mitigation: Check endpoint names and payloads before running actions that could spend credits, and use the credit-balance action when account cost exposure is relevant.

Risk: The oo CLI installation, OOMOL login, and Scrape Creators connection are persistent account setup steps.

Mitigation: Install only for agents intended to use the connected account, and run first-time setup steps only after matching authentication or connection failures.

## Reference(s):

- [Scrape Creators homepage](https://scrapecreators.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Scrape Creators ClawHub page](https://clawhub.ai/oomol/skills/oo-scrape-creators)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before endpoint invocation and returns connector responses as JSON.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
