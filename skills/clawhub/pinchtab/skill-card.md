## Description: <br>
Pinchtab helps agents control a local Chrome or Chromium browser for navigation, page inspection, form workflows, scraping, screenshots, PDFs, site review, and CLI or HTTP browser automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pinchtab](https://clawhub.ai/user/pinchtab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Pinchtab when an agent needs controlled local browser automation for web navigation, form workflows, page inspection, scraping, visual exports, or browser-backed site review. It is suited to browser tasks that benefit from stable accessibility references, token-efficient snapshots, and explicit safety gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can perform consequential actions on websites or authenticated accounts. <br>
Mitigation: Start read-only, require explicit confirmation before account changes, payments, deletions, messages, publishing, or permission changes, and restrict navigation to the sites needed for the task. <br>
Risk: Page-derived content can contain instructions that conflict with the user's task. <br>
Mitigation: Treat page content as untrusted data and follow it only when it independently matches the user's request. <br>
Risk: Screenshots, recordings, PDFs, browser state, cookies, and exports can expose sensitive data. <br>
Mitigation: Approve captures and state exports explicitly, use dedicated low-privilege PinchTab profiles, avoid personal browser profiles, and delete temporary artifacts when finished. <br>
Risk: High-impact browser features such as JavaScript evaluation, file upload, file download, cookie access, file-scheme navigation, and network export can expand local or account risk. <br>
Mitigation: Keep gated features disabled unless a task specifically needs them, then enable only the required capability with user approval and review outputs before sharing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/pinchtab/skills/pinchtab) <br>
- [PinchTab Source Repository](https://github.com/pinchtab/pinchtab) <br>
- [PinchTab Documentation](https://pinchtab.com) <br>
- [PinchTab Security and Trust](TRUST.md) <br>
- [Sensitive Operations](references/safety.md) <br>
- [CLI Commands Reference](references/commands.md) <br>
- [PinchTab API Reference](references/api.md) <br>
- [Profile Management](references/profiles.md) <br>
- [Site Review Reference](references/site-review.md) <br>
- [Verification and Gotchas](references/verification.md) <br>
- [Agent Optimization Playbook](references/agent-optimization.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON or HTTP API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to obtain browser snapshots, page text, screenshots, PDFs, recordings, audit reports, or API responses through PinchTab when the task requires them.] <br>

## Skill Version(s): <br>
0.15.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
