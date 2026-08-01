## Description: <br>
DataForSEO lets agents operate DataForSEO through OOMOL's oo CLI for backlink research, Google SEO and keyword workflows, Amazon merchant tasks, and account usage checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and SEO operators use this skill to run DataForSEO connector actions for backlink analysis, Google keyword and SERP research, Amazon merchant task submission and retrieval, and account usage checks through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing DataForSEO submit actions may create tasks and affect account usage or billing. <br>
Mitigation: Confirm the exact payload and intended effect with the user before approving any submit_* action. <br>
Risk: Setup or connection commands can be unnecessary when the oo CLI is already installed, signed in, and connected. <br>
Mitigation: Run setup or connection steps only after an oo CLI command fails with the matching auth, scope, connection, or billing error. <br>


## Reference(s): <br>
- [ClawHub DataForSEO Skill](https://clawhub.ai/oomol/skills/oo-dataforseo) <br>
- [DataForSEO Homepage](https://dataforseo.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas; write actions require user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
