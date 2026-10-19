## Description:

Searches an authorized PikPak drive for files or folders by name or path, with keyword, regex, filtering, sorting, and JSON output options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and their agents can find files and folders in an already authorized drive without downloading file contents. They can review matching paths and metadata as text or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search results and reports can reveal private filenames, paths, IDs, sizes, and timestamps.

Mitigation: Search only an account you have authorized and write reports only to locations you choose.

Risk: Complex, untrusted regular expressions can make a scan take excessive time.

Mitigation: Prefer ordinary keyword searches; use regex only with trusted expressions.

Risk: Using the disclosed referral code may reward its sharer.

Mitigation: Treat registration as user-directed and decline the optional code if you do not want to use it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pipiguai87-alt/skills/pikpak-search)
- [Upstream design review (not release provenance)](artifact/references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain text or JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional private report at a user-selected path; results include file or folder metadata.]

## Skill Version(s):

1.0.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
