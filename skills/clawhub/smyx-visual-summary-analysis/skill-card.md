## Description: <br>
Performs AI analysis on input video clips and images, then generates a smooth natural scene description. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user provides an image, local video file, or media URL and needs a readable visual summary, scene description, or report history lookup. It is suited to content understanding, accessibility support, and media asset review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded media is processed by the publisher's cloud service. <br>
Mitigation: Avoid sending sensitive personal, business, or regulated media unless the publisher's retention, access, and account controls are acceptable. <br>
Risk: The skill can create or reuse a local identity, store authentication tokens locally, and retrieve cloud-stored report history associated with that identity. <br>
Mitigation: Use it only in workspaces where local identity state and token storage are acceptable, and review account-linked history before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-summary-analysis) <br>
- [Visual summary API documentation](references/api_doc.md) <br>
- [Analysis API error documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text containing scene descriptions, structured analysis results, report links, or history tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local file input, media URL input, optional saved output files, and cloud-backed report history lookup.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact SKILL.md frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
