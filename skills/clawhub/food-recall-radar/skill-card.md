## Description:

Food Recall Radar helps an agent build and check a local pantry inventory against openFDA food recall data, then produce a risk-ranked action list for affected items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and household operators use this skill to maintain a pantry inventory, check it against active food recalls, and decide which items need package verification, discard, or return. Developers can also run offline checks against cached recall data for testing or scheduled household audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verbose live checks with an openFDA API key can expose the key in logs.

Mitigation: Avoid --verbose when using --api-key or OPENFDA_API_KEY; rotate the key if it was exposed in shared logs.

Risk: The pantry inventory and recall-hit history are stored locally and may reveal household purchase or health-sensitive context.

Mitigation: Use --file to choose an appropriate protected storage path and limit access to generated reports.

Risk: Fuzzy matching can produce false positives or miss recalls when brand, UPC, lot, or co-packer data is incomplete.

Mitigation: Confirm every hit and lot/date detail against the printed FDA notice, and treat no results as a point-in-time check rather than a permanent safety guarantee.

## Reference(s):

- [Food Recall Matching Methodology](references/recall-matching.md)
- [Sample Cached Recalls](references/sample-recalls.json)
- [openFDA Food Enforcement API](https://api.openfda.gov/food/enforcement.json)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/food-recall-radar)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and recall action summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local JSON pantry paths, cached recall data paths, FDA notice URLs, and VERIFY/MATCH/WATCH labels for human review.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
