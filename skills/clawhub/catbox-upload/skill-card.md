## Description: <br>
Upload files to catbox.moe for permanent hosting or litterbox.catbox.moe for temporary hosting and return the hosted file URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[microck](https://clawhub.ai/user/microck) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to upload a selected local file to Catbox for permanent sharing or Litterbox for temporary sharing. It is useful when an agent workflow needs to produce a shareable hosted file URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected files are uploaded to external Catbox or Litterbox hosting services and may become publicly accessible by URL. <br>
Mitigation: Upload only files intended for sharing, and do not upload secrets, private documents, credentials, or regulated data. <br>
Risk: Catbox uploads are permanent, and Catbox userhash values can be account-linked sensitive information. <br>
Mitigation: Prefer Litterbox for temporary sharing and treat any Catbox userhash as sensitive. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/microck/skills/catbox-upload) <br>
- [Catbox API Endpoint](https://catbox.moe/user/api.php) <br>
- [Litterbox API Endpoint](https://litterbox.catbox.moe/resources/internals/api.php) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text URL with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns the direct hosted file URL on success.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
