## Description: <br>
Analyzes gecko and lizard tail images or video to detect abnormal tail shortening, visible tail-tip wounds or scabs, and tail-loss event reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, breeders, and smart-vivarium developers use this skill to analyze supplied reptile tail images or videos, query historical reports, and receive structured tail-loss alerts with care-oriented guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends reptile images or media URLs to Life Emergence cloud APIs. <br>
Mitigation: Use only with media the user is allowed to upload, and disclose that analysis is cloud-connected rather than local-only. <br>
Risk: The skill silently creates or reuses an internal account identity and queries cloud history. <br>
Mitigation: Review account and history behavior before deployment, especially for shared workspaces or regulated environments. <br>
Risk: The skill stores account tokens in a local workspace SQLite database. <br>
Mitigation: Restrict workspace access, rotate or clear credentials when decommissioning, and avoid running it in untrusted shared directories. <br>
Risk: Visual analysis may produce unreliable or overstated tail-loss findings when images are incomplete, low resolution, poorly lit, or lack SVL/reference context. <br>
Mitigation: Require clear full-tail imagery and keep the documented unreliable-signal path for low-quality inputs instead of forcing a diagnosis. <br>
Risk: Care guidance could be mistaken for veterinary diagnosis or treatment. <br>
Mitigation: Keep outputs limited to visual observations and non-prescriptive guidance, and direct suspected infection or severe injury cases to a qualified reptile veterinarian. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, alert levels, tail-length measurements, wound indicators, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
