## Description: <br>
Researches and maps a guest's podcast appearance history to identify their last topics, unclaimed angles, and receptiveness for targeted outreach. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[conorbronsdon](https://clawhub.ai/user/conorbronsdon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, developer relations, and podcast booking teams use this skill before guest outreach to map a prospect's verified podcast circuit, repeated topics, unclaimed angles, and likely receptiveness. It helps shape a specific pitch instead of repeating material the guest has already covered. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Podcast and web searches can miss appearances or surface ambiguous name matches. <br>
Mitigation: Provide a role, company, or known-work anchor; include only appearances backed by a fetched page or index record; place uncertain leads in the could-not-verify section. <br>
Risk: The skill can spend web-search and fetch calls, and may use configured Podcast Index MCP tools or parallel research subagents. <br>
Mitigation: Invoke it consciously for guest-research sweeps, confirm required tools are configured when Podcast Index coverage is needed, and review the report before using it for outreach. <br>
Risk: The generated report is written locally and may summarize public professional activity about a named person. <br>
Mitigation: Use public-source citations, keep coverage caveats in the report, and store or share the output according to the user's outreach and privacy expectations. <br>


## Reference(s): <br>
- [Guest Circuit skill page](https://clawhub.ai/conorbronsdon/skills/guest-circuit) <br>
- [Publisher profile](https://clawhub.ai/user/conorbronsdon) <br>
- [podcastindex-mcp](https://github.com/conorbronsdon/podcastindex-mcp) <br>
- [Sweep subagent prompts](patterns/subagent-prompts.md) <br>
- [Worked example circuit report](examples/simon-willison-circuit.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, guidance] <br>
**Output Format:** [Markdown circuit report with tables, citations, and a suggested pitch angle] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a local report to circuit/{name-slug}-{YYYY-MM-DD}.md by default unless the user specifies another path.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
