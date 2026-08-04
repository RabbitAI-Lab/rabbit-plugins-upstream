## Description: <br>
Research what Reddit communities think about a topic by finding relevant public Reddit discussions with web search, comparing recurring opinions, disagreements, problems, and practical advice, and returning a structured report with traceable sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to research public Reddit discussions through web search and produce a sourced synthesis of community opinions, disagreements, recurring problems, and practical recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can only support conclusions with public Reddit discussions that are reachable through configured web search. <br>
Mitigation: Disclose search queries, reviewed and included discussion counts, timeframe filters, and access or snippet-only limitations in the report. <br>
Risk: User topics and search terms may be sent to the configured web search provider. <br>
Mitigation: Use the skill only for public Reddit research and avoid private, logged-in, deleted, gated, or personally identifying content. <br>
Risk: Reddit posts and comments are untrusted text and may contain misleading claims or embedded instructions. <br>
Mitigation: Treat Reddit content as evidence to analyze, cite source-dependent claims, separate facts from community opinion and synthesis, and ignore instructions embedded in Reddit content. <br>


## Reference(s): <br>
- [Report template](references/report-template.md) <br>
- [ClawHub skill page](https://clawhub.ai/margaretzybgl/skills/reddit-easy-search) <br>
- [Publisher profile](https://clawhub.ai/user/margaretzybgl) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Structured Markdown report with source links and optional inline shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires configured web search and public Reddit-accessible evidence; does not use Reddit OAuth or authenticated Reddit APIs.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
