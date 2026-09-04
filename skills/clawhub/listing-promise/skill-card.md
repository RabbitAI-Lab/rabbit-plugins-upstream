## Description:

Checks whether Amazon listing promises about features, effects, and usage match customer review evidence, then highlights evidence gaps; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare listing promises with ARI-collected Amazon review evidence and produce a focused operations report. It is intended for evidence review and operational guidance, not legal compliance conclusions, unsupported marketing copy, or automatic Amazon page changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release label is narrower than the artifact behavior: server security evidence says it is a broad ARI Amazon review and operations assistant, not only a listing promise checker.

Mitigation: Review the full command surface before use and deploy it only when the broader ARI assistant behavior is acceptable.

Risk: Some actions can spend ARI credits or use server-side auto-confirm policy.

Mitigation: Turn autoConfirm off when every paid action should be approved, and require quote review before running paid collection, analysis, leaderboard, operations, or advice commands.

Risk: Monitoring, competitor binding, exports, and workbench status commands can persist account-side changes or write local files.

Mitigation: Use explicit user approval for account changes, verify ASINs and watch IDs before management actions, and review export destinations before writing files.

Risk: The skill depends on an ARI API key and sends authenticated requests to ARI services.

Mitigation: Keep API keys out of reports and prompts, prefer setup/configuration flows that store keys locally, and check custom ARI base URL settings before sending authenticated requests.

## Reference(s):

- [ARI CLI and API Reference](artifact/references/reference.md)
- [Amazon Listing Promise Operation Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/listing-promise)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown reports, concise operational guidance, CLI commands, JSON API responses, and optional local CSV/Markdown/HTML exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ARI report IDs, report URLs, ASIN/site details, sample counts, credit usage, and local export paths.]

## Skill Version(s):

1.4.5 (source: server release evidence, SKILL.md frontmatter, _meta.json, and scripts/ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
