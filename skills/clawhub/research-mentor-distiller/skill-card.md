## Description: <br>
Distills public academic evidence about a researcher, lab, or research community into evidence-grounded mentor skill packages for research guidance and critique. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qwqalice](https://clawhub.ai/user/qwqalice) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and research teams use this skill to collect public academic evidence, synthesize research taste and methodology, and generate or validate mentor-style skill packages without claiming private beliefs or impersonating the target. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Academic source collection can include ambiguous, incomplete, or incorrect public metadata and PDFs. <br>
Mitigation: Review collection reports, fallback queues, and generated evidence snapshots before relying on the mentor profile. <br>
Risk: Generated mentor skills can overstate a real person's views or be installed before review. <br>
Mitigation: Keep direct evidence, strong inference, and speculative extension separate; validate generated packages and install only after explicit user approval. <br>
Risk: The publication collector includes an insecure SSL fallback for broken local certificate stores. <br>
Mitigation: Avoid the insecure SSL flag unless the operator understands the network risk and has no safer recovery route. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/qwqalice/MentorForge/tree/main/research-mentor-distiller) <br>
- [ClawHub skill page](https://clawhub.ai/qwqalice/skills/research-mentor-distiller) <br>
- [Compliance and Packaging](references/compliance-and-packaging.md) <br>
- [Full-Text Distillation Protocol](references/fulltext-distillation-protocol.md) <br>
- [Mentor Skill Template](references/mentor-skill-template.md) <br>
- [Profile Schema](references/profile-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown reports, JSON manifests, YAML agent configuration, Python script commands, and generated skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated mentor packages include evidence and validation references; installation is not automatic.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
