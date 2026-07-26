## Description: <br>
Tools Ui helps agents guide developers in adding React/Next.js tool lifecycle UI components from ui.inference.sh for tool calls, results, approvals, status indicators, and progress states. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to add or document tool-call displays, tool results, progress states, and human approval flows in React/Next.js agent interfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote setup commands may modify a React/Next.js project by installing components from an external registry. <br>
Mitigation: Review the referenced registry or source before running npx commands, consider pinning versions instead of using latest, and run setup only in projects you are comfortable modifying. <br>
Risk: Tool approval UI examples can affect how human-in-the-loop actions are presented to users. <br>
Mitigation: Review approval and denial behavior in the application before deploying workflows that can execute external tools or user-impacting actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/okaris/skills/tools-ui) <br>
- [ui.inference.sh](https://ui.inference.sh) <br>
- [Tools component registry](https://ui.inference.sh/r/tools.json) <br>
- [Tools component docs](https://ui.inference.sh/blocks/tools) <br>
- [Adding Tools to Agents](https://inference.sh/docs/agents/adding-tools) <br>
- [Human-in-the-Loop](https://inference.sh/docs/runtime/human-in-the-loop) <br>
- [Tool Approval Gates](https://inference.sh/blog/tools/approval-gates) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with bash and TSX code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes component imports, JSX examples, status descriptions, and setup commands for React/Next.js projects.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
