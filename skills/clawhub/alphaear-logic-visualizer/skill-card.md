## Description: <br>
Turns finance or investment logic into visual diagrams such as transmission chains, thesis maps, causal loops, risk/benefit paths, and Draw.io-compatible mxGraph XML or HTML artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and investment teams use this skill to convert structured or semi-structured finance theses into Draw.io diagrams for review and communication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: HTML diagram output can be written to caller-provided paths and may load the diagrams.net viewer from the internet when opened. <br>
Mitigation: Prefer XML output for fully local review, or constrain HTML output to a workspace directory before opening rendered files. <br>
Risk: Generated finance diagrams can overstate causal relationships if the input thesis is incomplete or speculative. <br>
Mitigation: Review node and edge assumptions, keep uncertain links labeled as assumptions, and avoid using the diagram as standalone investment advice. <br>


## Reference(s): <br>
- [AlphaEar Logic Visualizer Prompts](references/PROMPTS.md) <br>
- [ClawHub skill page](https://clawhub.ai/zoeluli7459-dev/skills/alphaear-logic-visualizer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, files, guidance] <br>
**Output Format:** [Draw.io mxGraph XML, HTML files, and concise Markdown explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [HTML diagram artifacts may load the diagrams.net viewer when opened.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
