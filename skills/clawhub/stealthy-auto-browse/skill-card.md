## Description: <br>
Headless-detection-resistant browser automation in Docker for authorized QA, compatibility testing, and defensive security research using Camoufox, OS-level input, and persistent fingerprints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and authorized security testers use this skill to drive browser automation against sites they own or have written permission to test, especially when validating anti-bot compatibility, false-positive blocks, and defensive test flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stealth-oriented browser automation can be misused outside authorized QA or security testing. <br>
Mitigation: Use it only for owned systems or targets with written authorization, and keep the test scope explicit before running actions. <br>
Risk: An exposed API or noVNC viewer can give remote users control of browser navigation, input, sessions, screenshots, and script execution. <br>
Mitigation: Bind service ports to localhost, set AUTH_TOKEN for anything beyond a throwaway local smoke test, and avoid publishing noVNC unless it is needed for local debugging. <br>
Risk: Persistent profiles, loader YAML, and external container images can preserve sensitive state or execute behavior the operator did not intend. <br>
Mitigation: Use dedicated test accounts, avoid persistent real sessions, review loader YAML before mounting it, and pin or review the Docker image before use. <br>
Risk: Dialog auto-accept and broad page capture actions can approve destructive prompts or collect more page data than the test requires. <br>
Mitigation: Disable or scope dialog acceptance before stateful actions, and collect only the text, DOM, screenshots, or logs needed for the authorized test. <br>


## Reference(s): <br>
- [Setup](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON action examples, YAML scripts, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying browser service can return page text, HTML excerpts, screenshots, recordings, cookies or storage data, network logs, console logs, and JSON script results depending on the invoked action.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
