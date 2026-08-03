## Description: <br>
Podcast-appearance research for guest booking. Use when asked to "map someone's podcast circuit," "where has X podcasted," "research X before guest outreach," or "find an unclaimed angle for X." Sweeps Podcast Index, web search, and the guest's own channels in parallel, then delivers a circuit report: appearance timeline, stump speech, unclaimed angles, receptiveness signal, and a specific pitch angle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, producers, and booking teams use this skill before guest outreach to map a prospective guest's podcast appearance history, identify repeated topics, find unclaimed angles, and draft a focused pitch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public-web research can drift into private dossier-building, contact scraping, or unrelated background checks. <br>
Mitigation: Use the skill only for public podcast-booking research and keep the scope tied to appearances, recent work, and outreach relevance. <br>
Risk: Search snippets or ambiguous matches can produce false appearances for people with similar names. <br>
Mitigation: Require an anchor fact, confirm every timeline entry with a fetched page or Podcast Index record, and keep unverified leads in a separate could-not-verify section. <br>
Risk: The workflow may create a Markdown report in the workspace. <br>
Mitigation: Review the requested output location and report contents before sharing or committing generated files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/conorbronsdon/skills/guest-circuit) <br>
- [README](artifact/README.md) <br>
- [Guest Circuit instructions](artifact/SKILL.md) <br>
- [Sweep subagent prompts](artifact/patterns/subagent-prompts.md) <br>
- [Worked circuit report example](artifact/examples/simon-willison-circuit.md) <br>
- [podcastindex-mcp](https://github.com/conorbronsdon/podcastindex-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with tables, source links, and a suggested pitch angle] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a dated circuit report to the workspace by default and shows the appearance timeline and suggested pitch inline for review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
