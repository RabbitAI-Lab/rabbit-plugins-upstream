## Description: <br>
Looks up IETF RFCs, checks whether specifications are current or obsolete, and reads targeted sections for accurate protocol citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shbernal](https://clawhub.ai/user/shbernal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical agents use this skill to find the relevant IETF RFC, confirm obsolescence or update status, and read only the sections needed to answer protocol questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal lookups may fetch public RFC files and cache them locally. <br>
Mitigation: Use the default mirror or a dedicated RFC directory rather than pointing --mirror or RFC_MIRROR at unrelated personal folders. <br>
Risk: Full-text mode can download about 512 MB when sync is explicitly run. <br>
Mitigation: Run sync only when full-text search is needed and the user has accepted the download. <br>


## Reference(s): <br>
- [RFC Editor index](https://www.rfc-editor.org/rfc-index.txt) <br>
- [RFC Editor RFC text endpoint](https://www.rfc-editor.org/rfc/rfc{number}.txt) <br>
- [Release changelog v0.2.4](https://github.com/shbernal/rfc-ai-tooling/releases/tag/v0.2.4) <br>
- [ClawHub skill page](https://clawhub.ai/shbernal/skills/rfc-lookup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May fetch and cache public RFC documents; full-text mirror sync is opt-in and approximately 512 MB.] <br>

## Skill Version(s): <br>
0.2.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
