## Description:

zmm-resonate helps solo knowledge creators diagnose whether drafts, viral examples, or raw observations have a clear resonance structure and actionable public angle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing assistants use this skill to diagnose draft resonance, decode why benchmark content works, and turn an observed phenomenon into a public-facing content angle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may activate the skill when the user only intended a casual resonance or virality discussion.

Mitigation: Use explicit triggers such as /zmm-resonate when invoking the skill, and confirm the intended mode when the request is ambiguous.

Risk: The skill may read local zmm reference or memory files and may save limited diagnostic lessons.

Mitigation: Install it only in workspaces where those local files are appropriate to use, and review any retained diagnostic memory for sensitive content.

Risk: Mode C can turn observations into broader public claims if supporting examples or facts are weak.

Mitigation: Keep public-problem framing tied to verified examples, and label unsupported mechanisms as working hypotheses rather than facts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-resonate)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown diagnostic reports with concise findings, concrete revision actions, and numbered next-step options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local zmm guidance and memory files when available; does not produce executable code.]

## Skill Version(s):

0.2.1 (source: server release evidence; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
