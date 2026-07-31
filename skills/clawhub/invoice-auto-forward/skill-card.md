## Description: <br>
Automatically scans supported mailboxes for invoice messages, parses PDF, OFD, or XML invoices, and helps forward matching invoices to configured finance, administrative, or archive recipients. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, finance teams, administrators, and workflow operators use this skill to configure and run mailbox-based invoice forwarding for reimbursement, archiving, and finance handoff workflows. It guides setup, dry-run scanning, confirmation before sending, and unattended scheduled runs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses user mailboxes and forwards invoice content to configured recipients. <br>
Mitigation: Use it only on mailboxes and invoices the user is authorized to process, verify forwarding and CC recipients, and dry-run with scan before run. <br>
Risk: Invoice download links may point outside the mailbox provider and could broaden network access. <br>
Mitigation: Prefer configuring link_domains, keep link size and timeout limits, and rely on the skill's invoice-format gate before forwarding downloaded content. <br>
Risk: Skipping connection verification can save incorrect or untested mailbox settings. <br>
Mitigation: Avoid --no-verify for normal setup and run check before unattended execution. <br>
Risk: Installing optional PDF dependencies into a shared Python environment can affect other projects. <br>
Mitigation: Install pdfplumber and pymupdf in a virtual environment when possible. <br>


## Reference(s): <br>
- [Configuration example](references/config.example.json) <br>
- [Troubleshooting and mailbox setup](references/troubleshooting.md) <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/invoice-auto-forward) <br>
- [Publisher profile](https://clawhub.ai/user/songhonglei) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local configuration, secrets, state, and report files when the user runs the bundled script.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release, CHANGELOG, script __version__; SKILL.md frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
