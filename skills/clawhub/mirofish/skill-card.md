## Description: <br>
Build MiroFish-style multi-agent prediction workflows offline by extracting seed structure, designing an ontology, writing a simulation plan, producing a forecast brief, and generating interview questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[y3519712124-ui](https://clawhub.ai/user/y3519712124-ui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to turn news, policy drafts, financial signals, or story material into an offline MiroFish-style prediction workflow with scenario structure, ontology, simulation planning, forecast branches, and interview prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live backend mode includes reset/delete actions and file-upload workflows when explicitly requested. <br>
Mitigation: Use live backend mode only when intentionally operating a MiroFish backend, review files before upload, and confirm destructive reset or delete actions before execution. <br>
Risk: The skill produces forecast branches and simulated-world analysis that may be mistaken for observed outcomes. <br>
Mitigation: Require outputs to distinguish observed facts, inferred branches, confidence, caveats, and uncertainty. <br>


## Reference(s): <br>
- [Mirofish ClawHub Skill Page](https://clawhub.ai/y3519712124-ui/skills/mirofish) <br>
- [Server-Resolved GitHub Provenance](https://github.com/y3519712124-ui/MiroFish-skills/tree/main/mirofish) <br>
- [Output Patterns](references/output-patterns.md) <br>
- [Worked Example](references/worked-example.md) <br>
- [Offline Playbook](references/offline-playbook.md) <br>
- [Workflow Map](references/workflow-map.md) <br>
- [API Surface](references/api-surface.md) <br>
- [Runtime Contract](references/runtime-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with structured sections and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline output should separate observed facts, inferred branches, and uncertainty; live backend details are only included when explicitly requested.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
