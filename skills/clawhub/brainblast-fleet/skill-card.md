## Description: <br>
Autonomous, scheduled agent that finds real, proven security footguns in popular SDKs and submits them to the open Brainblast corpus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dsb-117](https://clawhub.ai/user/dsb-117) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security engineers use this skill to run an autonomous OpenClaw fleet that searches public code for reproducible SDK security footguns, proves candidates locally, and submits proven findings to the Brainblast corpus. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run as a scheduled background job and execute a cloned Brainblast engine checkout. <br>
Mitigation: Review the default remote repository and cron settings before installation, and run it only in an environment where scheduled registry submission is intended. <br>
Risk: The managed checkout is reset during fleet runs. <br>
Mitigation: Do not point BRAINBLAST_REPO at a working repository; use the default managed checkout or a dedicated disposable directory. <br>
Risk: Optional ingest and reproof tokens affect registry submission and operator workflows. <br>
Mitigation: Provide optional tokens only when you trust the registry and operator workflow, and keep them scoped to the intended deployment. <br>


## Reference(s): <br>
- [Brainblast Registry](https://registry.brainblast.tech) <br>
- [ClawHub skill page](https://clawhub.ai/dsb-117/skills/brainblast-fleet) <br>
- [Brainblast engine repository](https://github.com/DSB-117/brainblast.git) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with shell command blocks and run summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires git, node, npm, and python3; supports optional environment variables for registry ingest, managed checkout location, and reproof.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
