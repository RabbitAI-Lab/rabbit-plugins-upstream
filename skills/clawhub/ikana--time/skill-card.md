## Description: <br>
LLM time reasoning scaffold with a bundled Node.js CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ikana](https://clawhub.ai/user/ikana) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to anchor date, deadline, scheduling, and relative-time reasoning in a local timeline before drafting plans or answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI writes a local time.md file and --force can overwrite an existing timeline. <br>
Mitigation: Run it in the intended project or a scratch directory, and use --force only when overwriting time.md is intentional. <br>
Risk: Timeline notes may capture sensitive project details if a user enters them. <br>
Mitigation: Do not store secrets or sensitive credentials in timeline event names or notes. <br>
Risk: Relative-time reasoning can become stale after NOW changes. <br>
Mitigation: Run the refresh command before relying on an existing time.md timeline. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ikana/time) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown timeline tables, local time.md files, stdout text, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js 18+. The bundled CLI is non-interactive, writes time.md in the current directory, prints timeline output to stdout, and writes warnings or errors to stderr.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
