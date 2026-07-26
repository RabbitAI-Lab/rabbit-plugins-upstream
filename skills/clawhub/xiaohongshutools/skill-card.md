## Description: <br>
XiaoHongShu (Little Red Book) data collection and interaction toolkit for searching notes, retrieving profiles, comments, likes, and trending content, with optional authenticated account actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chocomintx](https://clawhub.ai/user/chocomintx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to collect XiaoHongShu public content, inspect user and note data, and automate selected platform interactions. Authenticated use can act through a supplied web_session cookie and should be reviewed before operational deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated operation can give a local automation tool access to a XiaoHongShu session that can act as the user's account. <br>
Mitigation: Use non-critical accounts where possible, avoid pasting real web_session cookies into code, chats, or logs, and limit use to reviewed workflows. <br>
Risk: The artifact includes live interaction APIs such as follow, like, comment, and delete operations. <br>
Mitigation: Review mutation APIs before use, disable actions that are not required, and run with conservative rate limits. <br>
Risk: Security evidence flags underdocumented engagement-simulation and unsafe credential-handling patterns. <br>
Mitigation: Review or remove the read-count metrics workflow, cookie-bearing fingerprint fields, session-cookie logging, and eval-based config parser before operational use. <br>


## Reference(s): <br>
- [RedCrack](https://github.com/Cialle/RedCrack) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include XiaoHongShu API usage examples and credential-handling guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
