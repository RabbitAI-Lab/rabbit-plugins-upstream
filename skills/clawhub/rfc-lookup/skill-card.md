## Description: <br>
RFC lookup helps agents find IETF RFCs, read focused sections, check obsolescence, and cite current protocol specifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shbernal](https://clawhub.ai/user/shbernal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and technical writers use this skill to look up RFC metadata, locate relevant sections, and verify whether an RFC has been obsoleted before citing protocol requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal use may download public RFC data and cache it locally. <br>
Mitigation: Review the cache location before use and choose a dedicated mirror directory when overriding RFC_MIRROR or --mirror. <br>
Risk: Full mirror sync can download a large RFC corpus. <br>
Mitigation: Run sync only after an explicit user request and after explaining the download and local storage impact. <br>


## Reference(s): <br>
- [RFC Editor Index](https://www.rfc-editor.org/rfc-index.txt) <br>
- [RFC Editor text documents](https://www.rfc-editor.org/rfc/rfc{number}.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text with shell command examples and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May fetch public RFC documents on demand and may read or write a local RFC mirror when the user explicitly requests sync.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
