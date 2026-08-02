## Description: <br>
Routes academic paper workflows by identifying the discipline and production stage, then recommending the appropriate STEM or economics sub-skill without directly performing writing, analysis, network, subprocess, or file-writing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, academic writers, and agent operators use this skill to route paper-writing, submission, review, and revision requests into the correct STEM or economics workflow stage. It is best suited for coordinating installed paper-workflow sub-skills and preserving handoff context between stages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ambiguous academic-writing requests may be routed into publication sub-skills that handle sensitive drafts, data, or reviewer material. <br>
Mitigation: Confirm the selected branch, stage, and downstream sub-skill before sharing sensitive content. <br>
Risk: Downstream sub-skills may have their own permissions, licenses, and side effects even though this router is read-only. <br>
Mitigation: Review the target sub-skill's security and license information before allowing it to process project materials. <br>


## Reference(s): <br>
- [Skill Definition](SKILL.md) <br>
- [学科识别决策树与分支路由](references/discipline-routing.md) <br>
- [经济学分支工作流（E-0 ~ E-5）](references/econ-workflow.md) <br>
- [全部 40 个子 skill 速查表](references/skill-map.md) <br>
- [Sub-skill Protocol](references/sub-skill-protocol.md) <br>
- [阶段触发关键词完整表](references/trigger-map.md) <br>
- [STEM Branch Workflow Map](references/workflow-map.md) <br>
- [Optional Econ Extension Package](https://github.com/juliaError/econ-TopJournal-writing-Skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown or plain text routing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May name the branch, phase, target sub-skill, handoff inputs, and next step; the router itself does not directly create files, run commands, or call networks.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
