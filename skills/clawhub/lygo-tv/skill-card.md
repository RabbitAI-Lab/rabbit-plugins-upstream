## Description:

LYGO TV points agents and humans to the free online TV player at https://chatagent.ca/sources/ and provides local commands that print bookmark, URL, and JSON pointer information without fetching streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External users and agents use LYGO TV to direct people to a free online TV player, cite the canonical player URL, and print bookmark or catalog pointer information. The skill is a pointer package and does not fetch, proxy, decrypt, or publish streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat printed external URLs as covered by the local package isolation claim.

Mitigation: Treat the package as a pointer only; review any separate skill or process that fetches listed URLs because that behavior is outside this skill's local execution boundary.

Risk: Installers or downstream agents may fetch or execute unreviewed remote content.

Mitigation: Install in a low-privilege environment and prefer a pinned, reviewed ClawHub installer version when stricter supply-chain control is required.

Risk: The TV-player workflow could be misused to invent playlists, proxy streams, or imply working access where streams fail.

Mitigation: Keep behavior to bookmark and URL guidance; do not proxy, decrypt, invent channels, or mask dead streams, geo-blocks, and CORS misses.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/deepseekoracle/skills/lygo-tv)
- [LYGO TV player](https://chatagent.ca/sources/)
- [Catalog JSON](https://chatagent.ca/sources/catalog.json)
- [Configured player source](https://github.com/DeepSeekOracle/chatagent/tree/main/sources)
- [Configured skill repository](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/clawhub/mirrors/lygo-tv)
- [Security notes](references/SECURITY.md)
- [SkillSpector audit](references/SKILLSPECTOR_AUDIT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON pointer output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local scripts print URLs and pointer data only; no local network, subprocess, filesystem write, or publish behavior is declared.]

## Skill Version(s):

1.2.0 (source: frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
