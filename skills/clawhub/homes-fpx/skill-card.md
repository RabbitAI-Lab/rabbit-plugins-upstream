## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, history, and read signed-in saved homes through the user's own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve homes.com real-estate listing data from shell workflows when the MCP server is not installed or a one-shot browser-session-backed request is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in browser session and can access private homes.com account data such as saved homes and saved searches.

Mitigation: Run saved-home or saved-search commands only when intentional, keep the Transporter extension scoped to homes.com, and review the skill before installing.

Risk: Examples write homes.com data to fixed files under /tmp, which can expose private account or listing data on shared systems.

Mitigation: Use private mktemp directories with cleanup instead of shared fixed /tmp paths.

Risk: The security verdict is suspicious because browser-session access and temporary-file examples require operator review.

Mitigation: Use a pinned, trusted fpx version where possible and review the release before use.

## Reference(s):

- [homes.com request recipes](artifact/references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, JavaScript, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce HTML or JSON outputs from homes.com through fpx.]

## Skill Version(s):

1.4.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
