## Description: <br>
Analyzes reptile enclosure images or video frames to identify urate size, color, and texture plus feces morphology, then returns a structured visual assessment with alert guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, breeders, and enclosure app developers use this skill to analyze reptile excrement images or video frames, retrieve cloud report history, and generate structured visual-health observations with recommended next actions. The skill is framed as visual assessment support, not disease diagnosis or prescription guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile media and report history are processed by LifeEmergence cloud services. <br>
Mitigation: Use only media appropriate for cloud processing, avoid sensitive backgrounds or identifying information, and confirm data retention expectations before deployment. <br>
Risk: The skill can create or reuse a local identity and store service tokens in the workspace. <br>
Mitigation: Run it in a private, controlled workspace and remove the skill data directory or credentials when access is no longer needed. <br>
Risk: History queries can return identity-linked report records. <br>
Mitigation: Restrict use in shared environments and verify that the active workspace identity is the intended one before querying report history. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill source documentation](artifact/SKILL.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-excrement-analysis-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Files] <br>
**Output Format:** [Structured text or JSON with report fields, Markdown tables for history lists, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, alert levels, recommended actions, and disclaimers; depends on LifeEmergence cloud API responses.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
