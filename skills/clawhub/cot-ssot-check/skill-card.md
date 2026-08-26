## Description:

Single-source-of-truth drift auditor for documentation-heavy repos. Use when asked to "check for drift," "find copies of this number," "audit the docs for stale facts," or "set up an SSOT manifest." Finds facts hand-copied across files, builds a manifest of canonical locations, and verifies every copy still matches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to discover duplicated facts across prose files, propose a .ssot.yaml manifest, and check whether known copies still match their canonical source.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect private metrics or business facts in the current repository and sibling repositories when those paths are included in a manifest.

Mitigation: Review manifests and requested sibling paths before running the skill on sensitive repositories.

Risk: Generated fix proposals could update the wrong copy when a canonical value is stale or a counting convention differs.

Mitigation: Review proposed diffs and canonical assignments before applying any changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/cot-ssot-check)
- [Publisher profile](https://clawhub.ai/user/conorbronsdon)
- [README](artifact/README.md)
- [Discovery prompt pattern](artifact/patterns/discovery-prompt.md)
- [Worked discovery report](artifact/examples/cot-production-discovery/discovery-report.md)
- [Proposed SSOT manifest example](artifact/examples/cot-production-discovery/proposed-ssot.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown reports with proposed YAML manifest entries and inline diffs; no automatic repository edits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Discover mode proposes manifests for human approval. Check mode reports in-sync, drifted, moved, stale, and unverified facts.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
