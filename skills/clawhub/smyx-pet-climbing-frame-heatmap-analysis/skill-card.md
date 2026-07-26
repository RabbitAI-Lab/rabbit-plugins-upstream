## Description: <br>
Analyzes cat tree or pet climbing-frame videos and video URLs with server-side APIs to estimate layer dwell time, jumps or transitions, activity density, and a 2D activity heatmap without providing medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to submit cat tree area videos or URLs for structured activity heatmap analysis, history lookup, and report-link generation. Results are intended for activity observation and enrichment review, not health diagnosis or treatment guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cat-area videos, network video URLs, and analysis requests are sent to lifeemergence backend services. <br>
Mitigation: Avoid submitting videos or URLs that reveal people, private interiors, signed links, or other sensitive information unless the publisher provides acceptable privacy and retention terms. <br>
Risk: The skill can silently create or reuse an account-linked identifier and store tokens in the workspace data directory. <br>
Mitigation: Run the skill in an isolated workspace, review the publisher's account-control terms, and clear local workspace credentials when the skill is no longer needed. <br>
Risk: The output may describe activity and wellbeing trends but is not a veterinary diagnosis. <br>
Mitigation: Treat results as observational enrichment data and consult a qualified professional for medical or behavioral health decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis results, report links, or history listings; optionally saved to a local output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and json detail modes; input may be a local video file or a network video URL.] <br>

## Skill Version(s): <br>
1.0.5 (source: release evidence; artifact frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
