## Description: <br>
Search MuseScore sheet music, read score metadata, and resolve eligible download or PDF outputs through a configured MuseScore MCP setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search MuseScore scores, inspect score metadata, and obtain official download URLs or generated PDFs for free or otherwise entitled scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The referenced MCP server and fetchproxy extension operate through a signed-in MuseScore browser session. <br>
Mitigation: Install only components you trust, and use a dedicated browser or profile when tighter session containment is needed. <br>
Risk: Download and PDF actions may involve scores with access, purchase, or license restrictions. <br>
Mitigation: Request downloads or PDF generation only for scores you are entitled to access, and review returned score license metadata before reuse. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, URLs, metadata summaries, and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return MuseScore score metadata, official download URLs, and PDF file paths when available.] <br>

## Skill Version(s): <br>
0.15.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
