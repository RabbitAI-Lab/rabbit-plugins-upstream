## Description:

Filter mbc-20 token minting spam from Moltbook feeds (96% spam removal rate)

This skill is ready for commercial/non-commercial use.

## Publisher:

[ymode](https://clawhub.ai/user/ymode)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to scan Moltbook feeds, remove mbc-20 minting spam, and return cleaner feed results for review or downstream tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a local Moltbook API key and uses it for authenticated feed requests.

Mitigation: Use a limited-scope or read-only Moltbook API key if available, inspect the bundled JavaScript before use, and run the skill in a sandbox when stronger containment is needed.

Risk: Pattern-based spam filtering can miss changed spam formats or hide legitimate posts that match minting patterns.

Mitigation: Review scan output, tune the filter patterns for the current Moltbook feed, and avoid treating filtered results as an authoritative moderation decision.

## Reference(s):

- [Moltbook Spam Filter on ClawHub](https://clawhub.ai/ymode/skills/moltbook-filter)
- [Moltbook API endpoint](https://www.moltbook.com/api/v1)
- [Artifact README](artifact/README.md)
- [Skill documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON feed output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The feed command emits filtered JSON; the scan command emits a text feed analysis and sample clean posts.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
