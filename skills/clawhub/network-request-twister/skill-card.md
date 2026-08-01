## Description: <br>
Network Request Twister helps an agent observe, intercept, and modify browser network requests and responses through Chrome DevTools Protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[github-hewei](https://clawhub.ai/user/github-hewei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to inspect live browser HTTP traffic, mock API responses, block unwanted requests, and test web behavior under modified request or response conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can capture sensitive live browser traffic, including headers, cookies, request bodies, and response bodies. <br>
Mitigation: Use it only on sites and accounts you own or are authorized to test, avoid real credentials and production sessions, and prefer an isolated launched browser profile. <br>
Risk: Broad or incorrect interception rules can alter requests or responses beyond the intended test target. <br>
Mitigation: Scope rules to exact hosts, paths, methods, and resource types before enabling modification actions. <br>
Risk: The background interception process can continue exposing or modifying traffic while it remains active. <br>
Mitigation: Stop the running process immediately after observation or validation is complete. <br>


## Reference(s): <br>
- [Actions reference](artifact/references/actions.md) <br>
- [Conditions reference](artifact/references/conditions.md) <br>
- [Basic configuration example](artifact/examples/basic.json) <br>
- [Request modification example](artifact/examples/request-mod.json) <br>
- [Response modification example](artifact/examples/response-mod.json) <br>
- [ClawHub skill page](https://clawhub.ai/github-hewei/skills/network-request-twister) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration snippets, and JSONL observation output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May launch or attach to a browser debugging session and may keep a background process running until stopped.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter, pyproject.toml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
