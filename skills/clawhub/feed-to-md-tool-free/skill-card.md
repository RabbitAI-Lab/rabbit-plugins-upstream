## Description: <br>
Converts RSS or Atom feed content into structured Markdown documents by fetching feeds, parsing core fields, formatting entries, and saving files locally. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, individual users, and automation workflow authors use this skill to convert public RSS or Atom feeds into Markdown archives for reading, backup, and lightweight content organization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary flags broad activation scope beyond narrow RSS conversion requests. <br>
Mitigation: Enable or invoke the skill only for explicit RSS-to-Markdown tasks and review activation wording before installation. <br>
Risk: The skill can run Python, make outbound requests to RSS sources, install or use the requests library, and write Markdown plus metadata files locally. <br>
Mitigation: Use trusted feed URLs and caller-selected output directories, and inspect generated commands and file paths before execution. <br>


## Reference(s): <br>
- [Detailed RSS-to-Markdown examples](references/detail.md) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feed-to-md-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documents, Python snippets, shell commands, and local JSON metadata files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install or use the requests Python package, fetch caller-provided feed URLs, and write generated Markdown plus feed metadata to local output paths.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
