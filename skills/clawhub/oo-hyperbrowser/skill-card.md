## Description:

Hyperbrowser lets an agent fetch web pages, search the web, start crawls, and retrieve crawl results through a connected Hyperbrowser account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Hyperbrowser for web page fetching, web search, and crawl workflows while checking live action schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute local code if an agent runs them automatically or from unverified sources.

Mitigation: Install the oo CLI only through a verified, user-initiated process with trusted release provenance.

Risk: Starting a web crawl changes Hyperbrowser state and may consume account resources.

Mitigation: Confirm the exact crawl payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-hyperbrowser)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Hyperbrowser Homepage](https://www.hyperbrowser.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Schema-driven connector calls may return structured data with execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
