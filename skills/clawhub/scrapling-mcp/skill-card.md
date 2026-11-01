## Description:

Advanced web scraping with Scrapling - MCP-native guidance for extraction, crawling, and anti-bot handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devbd1](https://clawhub.ai/user/devbd1)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to configure Scrapling MCP access and choose scraping, extraction, crawling, and anti-bot handling patterns for authorized web automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scraping, proxy rotation, and anti-bot features may be misused against sites where the user lacks authorization.

Mitigation: Use the skill only on sites the user owns or is explicitly authorized to test, and respect site terms, robots.txt, rate limits, paywalls, authentication boundaries, and sensitive-data restrictions.

Risk: The skill can lead an agent to install dependencies, launch browser automation, fetch network content, save files, or remove crawl checkpoint directories.

Mitigation: Run it in a virtual environment or container, pin dependency versions where practical, and review generated commands, file paths, and cleanup operations before execution.

## Reference(s):

- [Scrapling references](references/links.md)
- [MCP Server Setup](references/mcp-setup.md)
- [Scrapling quick reference](references/api_reference.md)
- [Anti-bot handling](references/anti-bot.md)
- [Proxy Rotation](references/proxy-rotation.md)
- [Spider Recipes](references/spider-recipes.md)
- [Scrapling recipes](references/recipes.md)
- [Scrapling GitHub repository](https://github.com/D4Vinci/Scrapling)
- [Scrapling documentation](https://scrapling.readthedocs.io)
- [Scrapling MCP server documentation](https://scrapling.readthedocs.io/en/latest/ai/mcp-server/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to call the Scrapling MCP server or run local helper scripts for authorized scraping workflows.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
