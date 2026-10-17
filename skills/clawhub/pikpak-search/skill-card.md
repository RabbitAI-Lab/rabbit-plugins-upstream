## Description:

Searches file and folder names or paths across a PikPak account using local matching of directory listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pipiguai87-alt](https://clawhub.ai/user/pipiguai87-alt)

### License/Terms of Use:

MIT-0

## Use Case:

PikPak users and agents use this skill to find files or folders by name or path in an authorized account and optionally export matching metadata as JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Directory searches and saved reports can expose private file and folder metadata.

Mitigation: Use a specific folder for narrow searches and save reports only to intentionally selected paths.

Risk: Complex untrusted regular expressions can stall a search.

Mitigation: Prefer plain-text queries and avoid untrusted complex regex patterns.

Risk: A disclosed referral code may benefit the publisher if used during separate registration.

Mitigation: Decline the optional referral code when registering if you do not want to use it.

## Reference(s):

- [PikPak Search on ClawHub](https://clawhub.ai/pipiguai87-alt/skills/pikpak-search)
- [Upstream design and limitations](references/upstream-design.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable search results or a JSON report of matched file and folder metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include paths and may include IDs, sizes, and timestamps; reports are written only when requested.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
