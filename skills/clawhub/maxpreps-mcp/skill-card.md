## Description:

Read MaxPreps.com high school sports data - find a school, then get team schedules, scores, records, rosters, stat leaders, rankings, and athlete careers for any US high school.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up public MaxPreps high school sports information and convert MaxPreps page payloads into usable schedule, roster, ranking, stat, school, team, and athlete data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script keeps a MaxPreps build-id cache in the system temporary directory, which may be less private on shared machines.

Mitigation: On shared machines, move or patch the cache to a private user-owned cache directory before use.

Risk: MaxPreps page structure or positional payload keys may change, causing stale build IDs, 404s, or misaligned decoded data.

Mitigation: Use the bundled script's build-id refresh behavior and cross-check decoded schedules, rosters, and standings against independent page totals before relying on unusual results.

Risk: Public web lookups can fail or return incomplete season data when a team is out of season or a search query is too strict.

Mitigation: Resolve school and team paths before fetching, retry searches without qualifiers, and check prior seasons before reporting that data is absent.

## Reference(s):

- [MaxPreps recipes](references/recipes.md)
- [MaxPreps](https://www.maxpreps.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands; helper script outputs JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper script is read-only, uses public MaxPreps pages, and can decode local JSON from stdin.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
