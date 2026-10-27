## Description:

Analyzes short-fiction listings from Chinese reading platforms to help writers identify promising themes, emotional hooks, and story ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Short-fiction writers and editors use the skill to review platform listings, compare themes within each platform's own metrics, and choose story directions to test. When current listings are unavailable, it offers historical ideas as hypotheses rather than current trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Heiyan workflow uses an authenticated administrative browser session to access management data.

Mitigation: Review before installing if you use Heiyan. Run it only with an account whose backend access you are comfortable exposing to an agent-controlled Chrome session; skip Heiyan if you only intend to scan public listings.

Risk: Heiyan's book list does not show popularity, and historical notes cannot establish current trends.

Mitigation: Treat Heiyan listings as recently added titles, not a popularity ranking; verify historical ideas against dated current listings before relying on them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/story-short-scan)
- [Project link listed in skill metadata (not verified as release provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Dianzhong platform guide](artifact/references/platform-dianzhong.md)
- [Heiyan platform guide](artifact/references/platform-heiyan.md)
- [Manual listing input guide](artifact/references/manual-rank-input.md)
- [Historical market notes](artifact/references/real-market-data.md)
- [Story idea matching guide](artifact/references/topic-match.md)

## Skill Output:

**Output Type(s):** [Analysis, Writing guidance, Markdown]

**Output Format:** [Markdown report and story-idea recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample coverage, dates for reassessment, and source-based confidence notes.]

## Skill Version(s):

1.1.20 (source: ClawHub release metadata; bundled SKILL.md says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
