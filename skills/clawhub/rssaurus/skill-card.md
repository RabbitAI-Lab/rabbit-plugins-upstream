## Description: <br>
Use the RSSaurus command-line client (Go binary `rssaurus`) to interact with https://rssaurus.com from the terminal: authenticate (`rssaurus auth login/whoami`), list feeds/items, print item URLs for piping, open URLs, and perform triage actions (mark read/unread, bulk mark-read, save/unsave). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[justinburdett](https://clawhub.ai/user/justinburdett) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to have an agent run RSSaurus CLI workflows for feed review, item listing, URL extraction, and account triage actions. It is also useful when debugging RSSaurus CLI authentication or demonstrating safe command usage without exposing stored tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RSSaurus CLI configuration may contain API tokens if printed or shared. <br>
Mitigation: Avoid printing CLI config files; prefer re-authentication or sharing only non-sensitive error details. <br>
Risk: Bulk mark-read and save or unsave commands can modify the user's RSSaurus account state. <br>
Mitigation: Run account-changing commands only when the user intends those changes and confirm scope for bulk operations. <br>
Risk: The skill depends on a local `rssaurus` binary and an authenticated RSSaurus account. <br>
Mitigation: Verify the binary came from a trusted source and confirm authentication with `rssaurus auth whoami` before account workflows. <br>


## Reference(s): <br>
- [RSSaurus CLI repository](https://github.com/RSSaurus/rssaurus-cli) <br>
- [RSSaurus Homebrew tap](https://github.com/RSSaurus/tap) <br>
- [RSSaurus token creation](https://rssaurus.com/api_tokens/new) <br>
- [ClawHub skill page](https://clawhub.ai/justinburdett/skills/rssaurus) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request JSON output from the RSSaurus CLI when item IDs are needed for scripting or write actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
