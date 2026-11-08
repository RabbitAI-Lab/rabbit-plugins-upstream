## Description:

Search source code with a sparse n-gram index for fast literal or regex queries, repeated searches, and repository diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to search repositories for symbols, strings, configuration values, and errors, including repeated literal or regex searches. It helps initialize and refresh indexes and diagnose search setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The upstream search executable was not bundled or independently verified in this release.

Mitigation: Review and pin the upstream source before building the executable.

Risk: Indexes and search results can contain private source code or sensitive paths.

Mitigation: Index only intended repositories and keep indexes and search output private. Set SNGS_NO_STATS=1 to disable local usage statistics.

Risk: A cached dirty-worktree scan may temporarily miss recent file changes.

Mitigation: Run sngs sync when searches must reflect changes immediately, or set SNGS_SYNC_TTL_SECS=0 to disable the cache.

## Reference(s):

- [Sparse n-gram search project homepage](https://github.com/nano-harness/sparse-ngram-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text or JSON search results, with Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on repository filters and index freshness.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
