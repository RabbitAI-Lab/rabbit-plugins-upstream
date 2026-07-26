## Description: <br>
Extract a Hacker News post, linked article, comments, and key metadata into clean Markdown for quick reading or LLM input. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoqiao](https://clawhub.ai/user/guoqiao) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and users use this skill to turn a Hacker News item ID or URL into a single Markdown artifact containing the linked article, discussion thread, and metadata for review or downstream summarization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound web requests to Hacker News, Algolia, and linked article sites and downloads Python dependencies through uv. <br>
Mitigation: Use it only in environments where those network requests and dependency downloads are allowed. <br>
Risk: Generated Markdown contains web-derived article and comment content that may be incomplete, blocked, or unsuitable for automatic downstream use. <br>
Mitigation: Review the generated Markdown before relying on it for decisions or sending it into downstream workflows. <br>
Risk: The normal workflow can create and upload a generated extraction file. <br>
Mitigation: Handle the output file as external content and avoid including sensitive local data in the extraction path or follow-up message. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guoqiao/skills/hn-extract) <br>
- [Skill homepage](https://github.com/guoqiao/skills/blob/main/hn-extract/hn-extract/SKILL.md) <br>
- [Examples](https://github.com/guoqiao/skills/blob/main/hn-extract/examples) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown file or stdout with agent workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and Python 3.10 or newer; fetches Hacker News, Algolia, and linked article pages; may create an output Markdown file.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
