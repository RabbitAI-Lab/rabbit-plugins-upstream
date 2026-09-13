## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property detail, photos, and history, and read the signed-in user's saved homes through their own signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to produce shell-based homes.com request recipes and extraction commands when they need listing, property detail, photo, history, nearby listing, saved-home, or saved-search data without running the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes requests through a persistent signed-in homes.com browser session.

Mitigation: Use a dedicated browser profile when practical and install only if that browser-session access is acceptable.

Risk: Saved-homes and saved-searches recipes can pull personal account data into local files.

Mitigation: Run those recipes only when needed and delete downloaded authenticated pages after parsing.

Risk: Examples use predictable /tmp paths for downloaded pages and helper files.

Mitigation: Replace fixed temporary paths with a private mktemp directory before handling authenticated pages.

Risk: The setup installs the fpx CLI from npm.

Mitigation: Pin and verify npm package versions before installation.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub homes-fpx skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JavaScript, jq, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended to run through the user's fpx profile and signed-in homes.com browser session.]

## Skill Version(s):

1.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
