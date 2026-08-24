## Description:

Podcast-appearance research for guest booking that sweeps Podcast Index, web search, and the guest's own channels, then delivers a circuit report with an appearance timeline, repeated stump speech, unclaimed angles, receptiveness signal, and a specific pitch angle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conorbronsdon](https://clawhub.ai/user/conorbronsdon)

### License/Terms of Use:

MIT-0

## Use Case:

Podcast producers, guest bookers, and outreach teams use this skill before pitching a prospective guest to verify podcast appearances, avoid repeated topics, and identify an unclaimed angle for outreach.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Guest names and anchor facts may be sent to public search or podcast tools during research.

Mitigation: Use non-sensitive anchor facts and avoid running the sweep for private, embargoed, or confidential outreach targets unless the user accepts that exposure.

Risk: The workflow can make multiple web, podcast, or subagent calls.

Mitigation: Invoke it consciously for substantial guest-research sweeps and stop early if required tools or web access are unavailable.

Risk: Podcast appearance timelines can be misleading if based on snippets, name collisions, or model memory.

Mitigation: Include only appearances backed by fetched pages or index records, keep unresolved leads in a clearly labeled could-not-verify bucket, and require an anchor fact for disambiguation.

Risk: The skill writes a markdown report by default.

Mitigation: Direct the output path when needed and review the generated report before using it in outreach.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/conorbronsdon/skills/cot-guest-circuit)
- [Publisher profile](https://clawhub.ai/user/conorbronsdon)
- [README](artifact/README.md)
- [Sweep subagent prompts](artifact/patterns/subagent-prompts.md)
- [Worked circuit report example](artifact/examples/simon-willison-circuit.md)
- [podcastindex-mcp](https://github.com/conorbronsdon/podcastindex-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Markdown report with tables, links, source notes, and inline summary text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a saved circuit report by default and shows the appearance timeline plus suggested pitch angle inline for review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
