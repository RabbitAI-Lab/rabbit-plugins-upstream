## Description:

Helps agents filter community feed spam from digital-asset minting bots by scanning posts, matching content and author patterns, and guiding custom rules and blocklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scan community feeds or subboards, identify likely token-minting spam, produce a cleaned JSON feed, and maintain local filtering rules or blocklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a suspicious verdict because the skill asks for command/write capability and credential access while its scope and data-flow documentation are inconsistent.

Mitigation: Review before installing, run only in a sandboxed workspace for the community-feed filtering task, and avoid broad shell or write permissions.

Risk: Credential handling may expose API keys or local credential files if permissions are too broad.

Mitigation: Prefer environment variables or managed secrets over raw credential files, and grant only the minimum read access needed for the target platform.

Risk: Callback URLs may send filtered content or task metadata outside the local workspace.

Mitigation: Do not use callback URLs unless the destination and shared data are reviewed and acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/moltbook-filter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands, JavaScript snippets, and JSON feed output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include spam-rate summaries, clean-post lists, filtering rules, blocklist edits, and filtered feed JSON.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
