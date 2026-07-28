## Description: <br>
Implements and tests code while an independent reviewer challenges every change until all findings are reconciled. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[h0ngcha0](https://clawhub.ai/user/h0ngcha0) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use Hubo for explicitly invoked programming tasks where one agent implements and tests code while a separate read-only reviewer challenges changes until findings are reconciled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The work agent may edit files and the reviewer may inspect code and verification evidence. <br>
Mitigation: Invoke Hubo only on repositories where those actions are acceptable, and review the reported diff and checks before accepting the result. <br>
Risk: The two-role reconciliation workflow may take longer and produce verbose transcripts. <br>
Mitigation: Use Hubo when the extra review loop is worth the added time and transcript length for the programming task. <br>


## Reference(s): <br>
- [Hubo workflow](references/workflow.md) <br>
- [Host adapters](references/hosts.md) <br>
- [Karpathy-inspired coding discipline](https://github.com/multica-ai/andrej-karpathy-skills) <br>
- [Ponytail](https://github.com/DietrichGebert/ponytail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown conversation transcript with code, shell command, configuration, and verification details when the task requires them] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit invocation and may produce verbose multi-agent work and review transcripts.] <br>

## Skill Version(s): <br>
0.4.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
