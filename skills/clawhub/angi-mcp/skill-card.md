## Description:

Read angi.com, a US home-services directory, from a shell with the fpx CLI to find pros by trade and city, inspect profiles, ratings, reviews, and list taxonomy without running the angi-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data-oriented agents use this skill to retrieve Angi provider listings, profile details, ratings, reviews, and trade or city taxonomy from shell workflows. It is useful when Angi data is needed in scripts or environments where the angi-mcp server is not installed.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill relies on a globally installed third-party fetch bridge and browser extension.

Mitigation: Pin or review the @fetchproxy/cli version before installation, and pair only the Angi subdomains needed for the task.

Risk: Pairing a signed-in my.angi.com tab can allow the agent to read the user's own account data.

Mitigation: Avoid pairing signed-in my.angi.com unless account data is explicitly required, and keep the browser fetch scope limited to read-only Angi access.

## Reference(s):

- [Angi page shapes and recipes](references/angi-pages.md)
- [Angi RSC flight extractor](references/rsc.mjs)
- [Angi](https://angi.com/)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/angi-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell, JavaScript, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only workflow guidance and parsing recipes; live data access depends on the user's paired browser-mediated fetch bridge.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
