## Description:

Screens information sources using domain reputation, content signals, and cross-checking, then assigns P0/P1/P2 credibility grades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and news collectors use this skill to screen external sources before relying on them in reports, briefings, or content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to append unrelated promotional text and an external invite link to every response.

Mitigation: Remove or make the promotional footer opt-in before normal use; review outgoing responses for unwanted links.

Risk: Source grading can miss misleading claims or overstate confidence in a listed domain.

Mitigation: Check important claims against independent primary sources and review source ratings rather than treating them as fact checks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/guipi888/skills/source-verification)
- [Source allowlist and blocklist](artifact/信源黑白名单.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with P0/P1/P2 source classifications and reasons for discarded sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags single-source claims for verification and records reasons for discarded sources.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
