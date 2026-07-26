## Description: <br>
Persistent memory system for AI agents with automatic encoding, decay, and semantic reinforcement, based on Stanford Generative Agents (Park et al., 2023). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[impkind](https://clawhub.ai/user/impkind) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and OpenClaw agent builders use Hippocampus to add persistent, importance-weighted memory that can encode conversation signals, recall core memories, decay unused memories, and generate a local memory dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can retain sensitive personal details from conversations. <br>
Mitigation: Start with the default limited signal window, avoid --whole until reviewed, avoid sharing secrets in conversations, and inspect or delete memory files before enabling broader retention. <br>
Risk: Cron or background operation can repeatedly process conversation history without active review. <br>
Mitigation: Install without --with-cron first, review the generated memory files and OpenClaw cron commands, then enable scheduled processing only when the retention behavior is acceptable. <br>
Risk: The generated dashboard may expose local memory data or unintended avatar files. <br>
Mitigation: Keep brain-dashboard.html local, review IDENTITY.md avatar paths, and limit avatar paths to intended image files inside the workspace. <br>
Risk: Memory artifacts and event logs may be committed or shared accidentally. <br>
Mitigation: Add memory/index.json, pending memory files, brain-events.jsonl, HIPPOCAMPUS_CORE.md, and brain-dashboard.html to local ignore rules when they contain private data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/impkind/skills/hippocampus) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/impkind) <br>
- [Project repository declared in metadata](https://github.com/ImpKind/hippocampus-skill) <br>
- [Stanford Generative Agents paper](https://arxiv.org/abs/2304.03442) <br>
- [Generative Agents reference implementation](https://github.com/joonspk-research/generative_agents) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions, shell commands, JSON and JSONL memory files, generated Markdown core context, and a local HTML dashboard.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates local workspace memory artifacts such as memory/index.json, pending-memories.json, HIPPOCAMPUS_CORE.md, brain-events.jsonl, and brain-dashboard.html.] <br>

## Skill Version(s): <br>
3.9.0 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
