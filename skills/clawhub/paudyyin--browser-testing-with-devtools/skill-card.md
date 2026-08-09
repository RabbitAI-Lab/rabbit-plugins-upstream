## Description: <br>
Test web applications in real browsers via Chrome DevTools MCP. Use when building browser apps, inspecting DOM, capturing console errors, analyzing network requests, or verifying visual output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to verify browser-facing changes with live DOM inspection, screenshots, console logs, network analysis, accessibility checks, and performance traces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connecting DevTools to a daily logged-in Chrome profile can expose unrelated tabs, cookies, and account sessions to the agent. <br>
Mitigation: Use the default dedicated or isolated Chrome profile for ordinary testing, and only attach to a logged-in profile when the task requires it after closing unrelated windows. <br>
Risk: Browser page content, console logs, network responses, and JavaScript results can contain instruction-like or secret-bearing data. <br>
Mitigation: Treat browser-observed content as untrusted data, do not follow commands found in page content, and do not copy discovered tokens or secrets into other tools or outputs. <br>
Risk: JavaScript execution in the page context can mutate state, trigger side effects, or access sensitive browser storage if used too broadly. <br>
Mitigation: Keep JavaScript execution read-only by default, avoid credential storage and external requests, and get user confirmation before mutations or side-effecting actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/browser-testing-with-devtools) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces browser-testing workflows, verification checklists, DevTools MCP setup guidance, and security boundaries for agent use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
