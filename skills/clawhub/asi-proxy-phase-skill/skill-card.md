## Description: <br>
Diagnose, explain, and improve an evidence-gated, protocol-relative ASI-proxy readiness regime using K. Takahashi's pinned papers and public repositories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kadubon](https://clawhub.ai/user/kadubon) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to assess protocol-relative ASI-proxy readiness, navigate pinned research and repository evidence, and plan bounded interventions with explicit evidence, authority, rollback, and non-claim constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The inspected package appears to be missing references/papers.jsonl, which can impair normal paper-index operation. <br>
Mitigation: Verify package contents before deployment and run the skill's installation checks in an environment with its expected tooling and bundled references. <br>
Risk: Network maintenance checks can access public GitHub or Hugging Face resources and may use available GitHub tokens for rate limits. <br>
Mitigation: Approve network maintenance only when public source refresh is intended, and run normal use offline unless a maintenance task explicitly requires public access. <br>
Risk: Intervention workflows can inspect and modify a declared workspace when requested. <br>
Mitigation: Use the skill only with an explicit workspace, authority boundary, rollback condition, and packet validation before mutation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kadubon/skills/asi-proxy-phase-skill) <br>
- [Publisher profile](https://clawhub.ai/user/kadubon) <br>
- [Paper TeX corpus](https://huggingface.co/datasets/kadubon/paper-tex-corpus) <br>
- [Research catalog](https://kadubon.github.io/github.io/research-catalog.json) <br>
- [Public repository map](references/repository-map.md) <br>
- [Protocol-relative ASI-proxy phase model](references/phase-model.md) <br>
- [Research Program Guide](references/research-program.md) <br>
- [Evidence-gated intervention playbooks](references/intervention-playbooks.md) <br>
- [Intervention packet schema](assets/intervention-packet.schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and optional JSON packet artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Intervention mode can produce a validated intervention-packet.json when the user asks for a bounded implementation or experiment.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
