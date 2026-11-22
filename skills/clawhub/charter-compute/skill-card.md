## Description:

Rent a sandboxed machine by the hour and pay for it yourself in USDC on Base, with no account. Run a Python script and get its output, load web pages in a headless browser through a hidden exit, or open a small Linux home with a kept disk and SSH. Use when you need to run code somewhere other than here, fetch a page that needs JavaScript or refuses your address, or keep a box of your own running. 0.007 USDC an hour.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drew-dot-com](https://clawhub.ai/user/drew-dot-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can use this skill to run Python scripts on rented compute, fetch JavaScript-rendered pages, or access a small persistent Linux home over SSH. It provides the commands and operating guidance for those tasks, including payment and wallet limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned MCP package could change and execute locally without review; the security scan was partial, so evidence is incomplete.

Mitigation: Avoid installation until the package is pinned to a reviewed version. If proceeding, isolate the wallet from unrelated credentials and limit the funds it holds.

## Reference(s):

- [Charter agent documentation and pricing](https://charter.mainnet.toonprotocol.dev/agents)
- [Charter machine-readable documentation](https://charter.mainnet.toonprotocol.dev/llms.txt)
- [charter-mcp source repository](https://github.com/drew-dot-com/charter/tree/main/mcp)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Text, Guidance]

**Output Format:** [Markdown guidance with shell commands and descriptions of JSON and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses vary by task and may include command output, fetched page text, exit status, or lease details.]

## Skill Version(s):

0.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
