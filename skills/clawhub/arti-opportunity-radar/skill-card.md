## Description:

Build personalized stock-news briefings and opportunity scans from a user's holdings, watchlist, sectors, and selected sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[illli](https://clawhub.ai/user/illli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market researchers use this skill to configure stock interests, generate personalized market briefings, scan breaking news for related opportunities, and open verified events in ARTi for deeper per-stock analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save watchlist names, holdings names, themes, locale, timezone, and source choices in a hidden profile file in the current project.

Mitigation: It discloses the local profile path, asks for confirmation before writes or large changes, avoids broker credentials and account values, and supports profile review or deletion.

Risk: Finance-news summaries can be mistaken for investment advice or can overstate weak evidence.

Mitigation: It separates confirmed facts, reasonable inference, and unverified information; requires original or reliable secondary sources for key facts; includes counterconditions; and avoids target prices, trading instructions, or guaranteed moves.

Risk: Web pages, RSS feeds, announcement attachments, and aggregation summaries can contain untrusted text.

Mitigation: It treats source content as data, ignores instructions embedded in retrieved content, verifies important claims against authoritative sources, and reports important source access gaps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/illli/skills/arti-opportunity-radar)
- [Output Contract](artifact/references/output-contract.md)
- [Profile Schema](artifact/references/profile-schema.md)
- [Information Sources and Fallback Rules](artifact/references/sources.md)
- [ARTi Analysis Entry](https://artifin.ai/app/agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Files, Shell commands, Guidance]

**Output Format:** [Markdown briefings and analysis notes with evidence labels, source links, per-stock ARTi links, and optional local JSON profile updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Avoids trading instructions, target prices, guaranteed market outcomes, broker credentials, and account values.]

## Skill Version(s):

1.0.0 (source: server release metadata and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
