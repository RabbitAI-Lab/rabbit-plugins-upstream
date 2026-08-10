## Description: <br>
Turn a topic brief, research materials, vendor case, policy event, or industry question into a publish-ready single deep-dive article for technology, AI, data, cloud, or enterprise-software audiences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers, analysts, editors, and content teams use this skill to turn a single technology, AI, data, cloud, or enterprise-software topic into an evidence-backed Markdown article with planning, fact verification, originality review, human decision gates, review, and final packaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Drafts can contain unverified facts, stale dates, unsupported originality claims, or misleading framing if the fact table and human gates are skipped. <br>
Mitigation: Use the required fact table, originality review, Gate A planning confirmation, Gate B tension resolution, and final re-check before treating output as approved. <br>
Risk: Private writing profiles or source materials may contain sensitive details that should not be copied into a public article or generic skill package. <br>
Mitigation: Provide only intended source materials and writing-profile files, keep private profiles outside the public package, and run the machine gate that scans for credentials, personal paths, UUIDs, and publication metadata. <br>
Risk: The workflow is editorial and may produce publication-ready text, but it is not a publishing workflow. <br>
Mitigation: Stop at the approved final article and evidence package; route any layout, social copy, CMS, Notion, or external publishing action to a separate confirmed publishing process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/industry-deep-dive-pipeline-skill) <br>
- [Planning Schema](references/planning-schema.md) <br>
- [Evidence and Originality](references/evidence-and-originality.md) <br>
- [Writing Profile Interface](references/writing-profile-interface.md) <br>
- [Replay Evaluation](references/replay-evaluation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown case-bundle files, JSON machine-gate reports, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a local case directory ending at an approved final article and evidence package; it does not generate or execute publishing actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
